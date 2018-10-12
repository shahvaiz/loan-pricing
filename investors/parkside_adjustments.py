def calculate_adjustment_parkside(loan_amount, property_value, credit_score, loan_type, property_type, state, code):
	ltv_table_conforming = [
	[-.25, 0, 0, .25, .25, .25, .25, .25],
	[-.25, 0, .25, .5, .5, .5, .5, .5],
	[-.25, .5, .75, 1.125, 1.125, 1.125, 1.25, 1.25],
	[0, .5, 1.375, 2, 1.75, 1.5, 1.5, 1.25],
	[0, 1.125, 2.25, 2.75, 3, 2.5, 2.5, 2],
	[.5, 1.375, 2.75, 3.25, 3.5, 3, 3, 2.5]
	]

	ltv_table_conforming_cash_out = [
	[0, .25, .25, .5],
	[0, .625, .625, .75],
	[0, .625, .625, .75],
	[0, .75, .75, 1.375],
	[.25, .75, .75, 1.5],
	[.25, 1.25, 1.25, 2.25]
	]

	conforming_state = [
	[-.5, -.375],
	[-.5, -.375]
	]

	conforming_investment =[
	[1.75, 2],
	[3.125, 3.125],
	[3.875, 3.875]
	]

	
	hb_ltv_table = [
	[-.25, 0, 0, .25, .25, .25],
	[-.25, 0, .25, .5, .5, .5],
	[-.25, .5, .75, 1, 1, 1],
	[0, .5, 1.25, 1.75, 1.5, 1.25],
	[0, 1, 2, 2.5, 2.75, 2.25],
	[.5, 1.25, 2.5, 3, 3.25, 2.75]
	]

	hb_cash_out = [
	[1, 1.75],
	[1.25, 2]
	]

	hb_loan_amount = [
	[.25],
	[.2],
	[.18]
	]

	hb_state = [
	[-.5, -.375],
	[-.5, -.375]
	]

	hb_investment =[
	[1.75],
	[3.125]
	]

	jumbo3_fixed_a = [
	[-.75, -.625, -.25, 0, .25],
	[-.75, -.625, -.25, 0, .25],
	[-.625, -.375, -.125, .25, .5],
	[-.5, -.25, 0, .375, .625],
	[-.375, -.25, .125]
	]

	jumbo3_fixed_b = [
	[-.75, -.5, -.125, .125, .5],
	[-.75, -.5, 0, .125, .5],
	[-.625, -.125, .125, .375, .75],
	[-.5, -.125, .125, .625, 1]
	]

	jumbo3_fixed_c = [
	[-.625, -.375, 0],
	[-.625, -.375, .125],
	[-.5, 0, .25],
	[-.375, 0, .25]
	]

	jumbo3_fixed_d = [
	[-.625, -.375, 0],
	[-.625, -.375, .125],
	[-.5, 0, .25],
	[-.375, 0, .25]
	]

	jumbo3_fixed_second_home = [
	[0, .125, .375, 1]
	]

	jumbo3_fixed_purchase = [
	[-.25, -.25, -.25, -.125, 0]
	]

	jumbo3_fixed_cashout = [
	[.25, .25]
	]

	jumbo3fixed_waiver = [
	[.25],
	[.2],
	[.18]
	]

	jumbo1_arm_a = [
	[-.125, .375, .625],
	[-.25, .125, .375, .625, 1.25],
	[-.375, -.125, 0, .375, .875],
	[-.5, -.375, -.25, 0, .5]
	]

	jumbo1_arm_b = [
	[-.25, -.25, -.125, 0, 0],
	[-.25, 0, .125, .25, .375],
	[-.125, 0, .25]
	]

	jumbo1_arm_cash_out = [
	[.25, .25]
	]

	jumbo1_arm_second_home = [
	[.125, .25, .375, .75]
	]

	jumbo1_arm_purchase = [
	[-.375, -.375, -.375, -.375, -.375]
	]

	jumbo1arm_waiver = [
	[.25],
	[.2],
	[.18]
	]

	fha = [
	[0],
	[.125],
	[.25],
	[.75]
	]

	fha_loan_amount = [
	[1],
	[.125]
	]

	fha_state = [
	[.125],
	[0],
	[-.125]
	]

	fha_waiver = [
	[2],
	[1.45],
	[1],
	[.75],
	[.6],
	[.5],
	[.42],
	[2],
	[.35],
	[.3],
	[.25],
	[.2],
	[.18]
	]


	def row_credit_structure_a(credit_score):
		if credit_score >= 740:
			row = 0
		elif credit_score >= 720 and credit_score <= 739:
			row = 1
		elif credit_score >= 700 and credit_score <= 719:
			row = 2
		elif credit_score >= 680 and credit_score <= 699:
			row = 3
		elif credit_score >= 660 and credit_score <= 679:
			row = 4
		elif credit_score >= 640 and credit_score <= 659:
			row = 5
		return row

	def column_ltv_structure_a(ltv):	
		if ltv <= .6:
			column = 0
		elif ltv > .6 and ltv <= .7:
			column = 1
		elif ltv > .7 and ltv <= .75:
			column = 2
		elif ltv > .75 and ltv <= .8:
			column = 3
		elif ltv > .8 and ltv <= .85:
			column = 4
		elif ltv > .85 and ltv <= .9:
			column = 5
		elif ltv > .9 and ltv <= .95:
			column = 6
		elif ltv > .95 and ltv <= .97:
			column = 7
		return column

	def row_credit_structure_b(credit_score):
		if credit_score >= 800:
			row = 0
		if credit_score >= 760 and credit_score <= 799:
			row = 1
		elif credit_score >= 740 and credit_score <= 759:
			row = 2
		elif credit_score >= 720 and credit_score <= 739:
			row = 3
		elif credit_score >= 700 and credit_score <= 719:
			row = 4
		return row

	def column_ltv_structure_b(ltv):	
		if ltv <= .6:
			column = 0
		elif ltv > .6 and ltv <= .65:
			column = 1
		elif ltv > .65 and ltv <= .7:
			column = 2
		elif ltv > .7 and ltv <= .75:
			column = 3
		elif ltv > .75 and ltv <= .8:
			column = 4
		return column

	def row_credit_structure_c(credit_score):
		if credit_score >= 700 and credit_score <= 719:
			row = 0
		elif credit_score >= 720 and credit_score <= 739:
			row = 1
		elif credit_score >= 740 and credit_score <= 759:
			row = 2
		elif credit_score >= 760:
			row = 3
		return row

	def loan_amount_bucket(loan_amount):	
		if loan_amount <= 1000000:
			bucket = 0
		elif loan_amount > 1000000 and loan_amount <= 1500000:
			bucket = 1
		elif loan_amount > 1500000 and loan_amount <= 2000000:
			bucket = 2
		elif loan_amount > 2000000 and loan_amount <= 2500000:
			bucket = 3
		return bucket

	adj = 0

	loan_amount = float(loan_amount)
	property_value = float(property_value)
	ltv = loan_amount / property_value
	
	#code = '3510'
	
	if code == '3510' or code == '3519':
		

		#ltv/credit adjustment
		if loan_type != 'refi_cash_out':

			try:
				adj = adj + ltv_table_conforming[row_credit_structure_a(credit_score)][column_ltv_structure_a(ltv)]
				#import pdb; pdb.set_trace()
			except:
				adj = None


		else:
			try:
				adj = adj + ltv_table_conforming_cash_out[row_credit_structure_a(credit_score)][column_ltv_structure_a(ltv)]
			except:
				adj = None

		#state adjustment
		if state == 'maryland' or 'district of columbia':
			try:
				adj = adj + conforming_state[0][0]
			except:
				adj = None
		else:
			try:
				adj = adj + conforming_state[1][0]
			except:
				adj = None

		#investment property adjustment
		if property_type == 'investment':
			try:	
				if column_ltv_structure_a(ltv) <= 2:
					adj = adj + conforming_investment[0][0]
				elif column_ltv_structure_a(ltv) == 3:
					adj = adj + conforming_investment[1][0]	
				elif column_ltv_structure_a(ltv) == 4:
					adj = adj + conforming_investment[2][0]
				else:
					adj = None
			except:
				adj = None
		#return adj

	elif code == '3531' or code == '3532' or code == '3535':
		
		#ltv/credit adjustment
		if loan_type != 'refi_cash_out':

			try:
				adj = adj + hb_ltv_table[row_credit_structure_a(credit_score)][column_ltv_structure_a(ltv)]
			except:
				adj = None

		else:
			try:
				# Cash out, fixed
				if (code == '3531' or code == '3532') and ltv <= .6 and credit_score >= 680:
					adj = adj + hb_cash_out[0][0]
					#a = hb_cash_out[0][0]
					#import pdb; pdb.set_trace()
				
				# Cash out, fixed
				elif (code == '3531' or code == '3532') and ltv <= .6 and credit_score >= 640 and credit_score <=679:
					adj = adj + hb_cash_out[1][0]

				# Cash out, ARM
				elif (code == '3535') and ltv <= .6 and credit_score >= 680:
					adj = adj + hb_cash_out[0][1]

				# Cash out, ARM
				elif (code == '3535') and ltv <= .6 and credit_score >= 640 and credit_score <=679:
					adj = adj + hb_cash_out[1][1]
				
				# Not within the guidelines
				else:
					adj = None
			except:
				adj = None

		#state adjustment
		if state == 'maryland' or 'district of columbia':
			try:
				adj = adj + hb_state[0][0]
			except:
				adj = None
		else:
			try:
				adj = adj + hb_state[0][1]
			except:
				adj = None

		#investment property adjustment
		if property_type == 'investment':
			try:	
				if column_ltv_structure_a(ltv) <= 2:
					adj = adj + hb_investment[0][0]
				else:
					adj = None
			except:
				adj = None
		#return adj

	#Jumbo III, 30 year fixed
	elif code == '5521':
		
		#ltv/credit adjustment
		try:
			if loan_amount_bucket(loan_amount) == 0:
				adj = adj + jumbo3_fixed_a[row_credit_structure_b(credit_score)][column_ltv_structure_b(ltv)]
			elif loan_amount_bucket(loan_amount) == 1:
				adj = adj + jumbo3_fixed_b[row_credit_structure_b(credit_score)][column_ltv_structure_b(ltv)]
			elif loan_amount_bucket(loan_amount) == 2:
				adj = adj + jumbo3_fixed_c[row_credit_structure_b(credit_score)][column_ltv_structure_b(ltv)]
			elif loan_amount_bucket(loan_amount) == 3:
				adj = adj + jumbo3_fixed_d[row_credit_structure_b(credit_score)][column_ltv_structure_b(ltv)]
			else:
				adj = None
		except:
			adj = None

		#second home adjustment
		if property_type == 'second':
			try:	
				adj = adj + jumbo3_fixed_second_home[0][column_ltv_structure_b(ltv)]
			except:
				adj = None

		elif property_type == 'investment':
			adj = None

		#purchase adjustment
		if loan_type == 'purchase':
			try:	
				adj = adj + jumbo3_fixed_purchase[0][column_ltv_structure_b(ltv)]
			except:
				adj = None

		#cash out adjustment
		if loan_type == 'refi_cash_out':
			try:	
				adj = adj + jumbo3_fixed_cashout[0][column_ltv_structure_b(ltv)]
			except:
				adj = None

		#return adj

	#Jumbo I, 5/1 ARM
	elif code == '5505':
		
		try:
			adj = adj + jumbo1_arm_a[row_credit_structure_c(credit_score)][column_ltv_structure_b(ltv)]
		except:
			adj = None

		#ltv/credit adjustment
		try:
			adj = adj + jumbo1_arm_b[loan_amount_bucket(loan_amount)][column_ltv_structure_b(ltv)]
		except:
			adj = None

		#cash out adjustment
		if loan_type == 'refi_cash_out':
			try:	
				adj = adj + jumbo1_arm_cash_out[0][column_ltv_structure_b(ltv)]
			except:
				adj = None

		
		#second home adjustment
		if property_type == 'second':
			try:	
				adj = adj + jumbo1_arm_second_home[0][column_ltv_structure_b(ltv)]
			except:
				adj = None

		elif property_type == 'investment':
			adj = None

		#purchase adjustment
		if loan_type == 'purchase':
			try:	
				adj = adj + jumbo1_arm_purchase[0][column_ltv_structure_b(ltv)]
			except:
				adj = None

		#return adj
		#import pdb; pdb.set_trace()

	return adj
