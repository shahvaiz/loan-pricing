from myapp.models import CountyFees
from myapp.models import RegionInfo
import math

def county_convert(zip_code):
	return RegionInfo.objects.filter(zip = zip_code).values("county").distinct()
	#return RegionInfo.objects.filter(zip = zip_code)

def state_convert(zip_code):
	return RegionInfo.objects.filter(zip = zip_code).values("state").distinct()

def payment (loan_amount, interest_rate, months):
 	payment = loan_amount * (interest_rate/12 * math.pow((1+interest_rate/12),months)) / (math.pow((1+interest_rate/12),months) - 1)
 	return round(payment,2)

def apr (loan_amount, costs, interest_rate, months):

	payment_amount =  payment (loan_amount, interest_rate, months)
	loan_size =  loan_amount - costs
	apr_lower = 1.0/1200.0
	apr_upper = 70.0/1200.0
	midpoint = (apr_lower + apr_upper) / 2.0
	total = None
	total=0

	while (total < loan_size or total > (loan_size + .9999)):

		if (total < loan_size):

			apr_upper = midpoint
			midpoint = (apr_lower + apr_upper) / 2.0
			total = 0.0

			for t in range (1,months):
				total = total + payment_amount/ math.pow(1+midpoint, t)

		elif (total > loan_size):

			apr_lower = midpoint
			midpoint = (apr_lower + apr_upper) / 2.0
			total = 0.0

			for t in range (1,months):
				total = total + payment_amount/ math.pow(1+ midpoint,t)

	return round(midpoint * 1200.0, 3)


def ammortization (loan_amount, interest_rate, months):

	counter = 0
	balance = loan_amount
	total_interest = 0.0
	total_principal = 0.0
	ammortization_schedule = []

	while (balance > 0):

		old_balance = balance
		payment_amount =  payment (loan_amount, interest_rate, months)
		interest = balance * interest_rate/12
		balance = balance + interest - payment_amount
		counter = counter + 1;

		if (balance < 0):
			balance = 0

		total_interest = total_interest + interest
		principal = old_balance - balance
		total_principal = total_principal + principal
		total_paid = total_principal + total_interest
		ammortization_schedule.append ([payment_amount, balance, interest, total_interest, principal, total_principal, total_paid])
	return ammortization_schedule
