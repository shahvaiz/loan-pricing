from myapp.models import CountyFees


class State:
	abstract = 0  # 110 in md, dc, 85 in va
	courier = 65
	deed = 0  # md, va = 80, dc = 290
	payoff = 0
	settlement = 295
	title_examination = 95

	title_rates = [
		[4.67, 3.97, 3.34, 2.65],
		[2.78, 2.21, 1.94, 1.68],
		[4.68, 4.44, 4.08, 2.7],
		[2.9, 2.7, 2.3, 1.85],
		[6.84, 6.12, 5.4, 4.5],
		[5.4, 4.68, 3.96, 2.8]
	]

	limits = [250000, 500000, 1000000]

	def title_insurance(self, property_value, type):
		limits = State.limits

		tier1 = min(property_value/1000 * self.title_rates[type][0], limits[0]/1000 * self.title_rates[type][0])
		tier2 = min((property_value - limits[0])/1000 * self.title_rates[type][1], limits[0]/1000 * self.title_rates[type][1])
		tier3 = min((property_value - limits[1])/1000 * self.title_rates[type][2], limits[1]/1000 * self.title_rates[type][2])
		tier4 = (property_value - limits[2]) / 1000 * self.title_rates[type][3]

		if (property_value <= limits[0]):
			cost = tier1
		elif (property_value > limits[0] and property_value <= limits[1]):
			cost = tier1 + tier2
		elif (property_value > limits[1] and property_value <= limits[2]):
			cost = tier1 + tier2 + tier3
		elif (property_value > limits[2]):
			cost = tier1+ tier2 + tier3 + tier4
		return cost

	def rec (self, amount, rate):
		cost = float(rate) * (amount/1000)
		return cost

	def tax (self, amount, rate):
		cost = float(rate/100) * amount
		return cost


class MD (State):
	abstract = 110
	deed = 80
	payoff = 99
	purchase_tax = .5

	def __init__(self, county_name):
		county_row = CountyFees.objects.filter(county = county_name)
		for x in county_row:
			self.county_recording_rate = float(x.recording)
			self.county_tax_rate = float(x.taxes)

	# purchase: amount1 = loan amount, amount 2 = property value
	# refinance: amount1 = loan balance, amount 2 = loan amount
	def recording(self, amount1, amount2, county, loan_type, property_type):
		special_montgomery = 10.0;

		if (loan_type == 'purchase' and county == 'Montgomery'):
			if (amount2 > 500000 and property_type == 'primary'):
				recording_costs = self.rec(450000, self.county_recording_rate) + self.rec(amount2 - 500000, special_montgomery)

			elif(amount2 <= 500000 and property_type == 'primary'):
				recording_costs = self.rec(amount2 - 50000, self.county_recording_rate)

			elif (amount2 > 500000 and property_type != 'primary'):
				recording_costs = self.rec(500000, self.county_recording_rate) + self.rec(amount2 - 500000, special_montgomery)

			elif (amount2 <= 500000 and property_type != 'primary'):
				recording_costs = self.rec(amount2, self.county_recording_rate)

			recording_costs = recording_costs/2

		elif(loan_type == 'purchase' and county != 'Montgomery'):
			recording_costs = self.rec(amount2, self.county_recording_rate)
			recording_costs = recording_costs/2

		elif(loan_type == 'refi_rate_term' or loan_type == 'refi_cash_out'):
			if property_type == 'primary':
				recording_costs = self.rec(amount2 - amount1, self.county_recording_rate)
			else:
				recording_costs = self.rec(amount2, self.county_recording_rate)
		return recording_costs


	def purchase (self, loan_amount, property_value, county, loan_type, property_type):

		total = [self.recording (loan_amount, property_value, county, loan_type, property_type), self.tax(property_value, self.county_tax_rate)/2, self.tax(property_value, self.purchase_tax)/2, self.title_insurance(property_value, 0), self.abstract, self.deed, self.courier, self.settlement, self.title_examination, self.county_recording_rate,self.county_tax_rate]
		return total

	def refinance (self, balance, loan_amount, county, loan_type, property_type):

		total = [self.recording (balance, loan_amount, county, loan_type, property_type), self.title_insurance(loan_amount, 1),  self.abstract,  self.deed, self.courier, self.payoff, self.settlement, self.title_examination]
		#import pdb; pdb.set_trace()
		return total

class VA (State):
	abstract = 85
	deed = 80
	payoff = 99
	deed_tax = 3.3 # purchase price
	trust_tax = 3.3	# loan amount


	def purchase (self, loan_amount, property_value, loan_type):
		total = [self.rec (loan_amount, self.deed_tax), self.rec (property_value, self.trust_tax), self.title_insurance(property_value, 2), self.abstract, self.courier, self.deed, self.settlement, self.title_examination]
		return total

	def refinance (self, loan_amount):
		total = [self.rec(loan_amount, self.trust_tax), self.title_insurance(loan_amount, 3), self.abstract, self.courier, self.payoff, self.settlement, self.title_examination]
		return total


class DC (State):
	abstract = 110
	deed = 290
	payoff = 215

	deed_rate_a = 1.1
	deed_rate_b = 1.45

	def deed_calc(self, property_value):
		if (property_value <= 400000):
			deed_transfer = self.tax(property_value, self.deed_rate_a)
		elif (property_value > 400000):
			deed_transfer = self.tax(property_value, self.deed_rate_b)
		return deed_transfer

	def purchase (self, property_value):
		total = [self.deed_calc(property_value), self.title_insurance(property_value, 4),  self.abstract, self.courier, self.deed, self.settlement, self.title_examination]
		return total

	def refinance (self, property_value):
		total = [self.title_insurance(property_value, 5), self.payoff, self.abstract, self.courier, self.settlement, self.title_examination]
		return total
