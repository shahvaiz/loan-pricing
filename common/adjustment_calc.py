from investors.parkside_adjustments import *


def investor_adjustment(investor, loan_amount, property_value, credit_score, loan_type, property_type, state, prog_id):

	if investor == "impac":
		return calculate_adjustment_impac(loan_amount, property_value, credit_score, loan_type, property_type, state)

	elif investor == "parkside":
		# import pdb; pdb.set_trace()
		# hi = calculate_adjustment_parkside(loan_amount,
		# property_value, credit_score, loan_type, property_type, state, prog_id)
		return calculate_adjustment_parkside(loan_amount, property_value, credit_score, loan_type, property_type, state,
											prog_id)

	elif investor == "stearns":
		return calculate_adjustment_stearns(prog_id, loan_amount, property_value, credit_score, loan_type, property_type)

