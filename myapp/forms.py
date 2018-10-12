from django import forms
from django.core.validators import RegexValidator

class ContactForm(forms.Form):
	#loan_type = forms.ChoiceField(choices=[('purchase', 'Purchase'), ('refi_rate_term','Refinance: Rate & Term'),  ('refi_cash_out','Refinance: Cash Out')], widget = forms.Select(attrs={'onchange':'yesNo();', 'id': 'loan_type_s'}))
	loan_type = forms.ChoiceField(choices=[ ('refi_rate_term','Refi: Rate & Term'),  ('refi_cash_out','Refi: Cash Out'), ('purchase', 'Purchase'),], widget = forms.Select(attrs={'onchange':'yesNo();', 'class':'dropdown'}))
	loan_balance = forms.FloatField(required = False, widget=forms.TextInput(attrs={'placeholder':'Current Loan Balance'}), initial=250000)
	#loan_amount = forms.FloatField(widget=forms.TextInput(attrs={'placeholder':'Loan Amount'}))
	property_value = forms.FloatField(widget=forms.TextInput(attrs={'placeholder':'Property Value'}), initial=400000)
	down_payment = forms.FloatField(widget=forms.TextInput(attrs={'placeholder':'Down Payment'}), initial=120000)
	cash_out = forms.FloatField(widget=forms.TextInput(attrs={'placeholder':'Cash Out Amount'}), initial=20000)
	#purchase_price = forms.FloatField(widget=forms.TextInput(attrs={'placeholder':'Purchase Price'}))
	zip_code = forms.CharField(max_length = 5, widget=forms.TextInput(attrs={'placeholder':'Zip Code'}), initial=20854)
	#credit_score = forms.IntegerField(max_value = 900, min_value = 300, widget=forms.TextInput(attrs={'placeholder':'Credit Score'}))
	property_type = forms.ChoiceField(choices=[('primary', 'Primary Residence'), ('second','Second Home'),  ('investment','Investment Property')], widget = forms.Select(attrs={'class':'dropdown'}))


	# def clean_loan_balance(self):
	# 	amt = self.cleaned_data['loan_balance']
	# 	if amt!=None:
	# 		if amt < 50000:
	# 			raise forms.ValidationError("The minimum loan balance is $50,000")
	# 		if amt > 3000000:
	# 			raise forms.ValidationError("The maximum loan balance is $3,000,000")
	# 		return amt


	# def clean(self):
	# 	data = self.cleaned_data
	# 	if data.get('loan_balance'):
	# 		return data

	# def clean_loan_amount(self):
	# 	amt = self.cleaned_data['loan_amount']
	# 	if amt < 50000:
	# 		raise forms.ValidationError("The minimum loan amount is $50,000")
	# 	if amt > 3000000:
	# 		raise forms.ValidationError("The maximum loan amount is $3,000,000")
	# 	return amt

	# def clean_property_value(self):
	# 	amt = self.cleaned_data['property_value']
	# 	if amt < 50000:
	# 		raise forms.ValidationError("The minimum property value is $50,000")
	# 	if amt > 5000000:
	# 		raise forms.ValidationError("The maximum property value is $5,000,000")
	# 	return amt

	# def clean_cash_out(self):
	# 	amt = self.cleaned_data['cash_out']
	# 	if amt < 1000:
	# 		raise forms.ValidationError("The minimum cash out amount is $1,000")
	# 	if amt > 1000000:
	# 		raise forms.ValidationError("The maximum cash out amount is $1,000,000")
	# 	return amt


class CalculatorForm(forms.Form):
	loan_amount_calculator = forms.FloatField(widget=forms.TextInput(attrs={'placeholder':'Loan Amount'}), initial = 200000)
	interest_rate = forms.FloatField(widget=forms.TextInput(attrs={'placeholder':'Interest Rate'}), initial = 4.125)
	months = forms.ChoiceField(choices=[(40, '40 Years'), (30, '30 Years'), (20, '20 Years'),(15,'15 Years'),  (10,'10 Years'),  (5,'5 Years')], widget = forms.Select(attrs={'class':'dropdown'}), initial = 30 )
	#months = forms.FloatField(widget=forms.TextInput(attrs={'placeholder':'Months'}), initial = 360)
	#months = forms.ChoiceField(choices=[(30, '30'), (15,'15'),  (10,'10')], widget = forms.Select(attrs={'class':'dropdown'}))

#class CustomerForm(forms.Form):
  #   first_name = forms.CharField(label='First Name')
  #   last_name = forms.CharField(label='Last Name', max_length=20)
  #   phone_number = forms.CharField(label='Phone Number', max_length=13)
  #   email = forms.EmailField(label='Email Address')
  #   dob = forms.DateField(label='Date of Birth')
  #   ssn = forms.CharField(label='Social Security Number', max_length=12)
  #   credit_score = forms.IntegerField(max_value = 900, min_value = 300)
  #   loan_balance_2 = forms.DecimalField(max_digits=5, decimal_places=2)
  #   credit_score = forms.IntegerField(max_value = 900, min_value = 300)

  #   def clean_loan_balance_2(self):
		# amt = self.cleaned_data['loan_balance_2']
		# if amt!=None:
		# 	if amt < 50000:
		# 		raise forms.ValidationError("The minimum loan balance is $50,000")
		# 	if amt > 3000000:
		# 		raise forms.ValidationError("The maximum loan balance is $3,000,000")
		# 	return amt


class ApplicationForm(forms.Form):
	first_name = forms.CharField() # do not validate names
	last_name = forms.CharField() # do not validate names
	phone_number = forms.CharField(label='Phone Number', validators=[
            RegexValidator(
                # http://stackoverflow.com/questions/123559/a-comprehensive-regex-for-phone-number-validation
                regex='^(?:(?:\+?1\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?$',
                message='Invalid phone number',
            ),
        ])
	email = forms.EmailField(required=False)
	#dob = forms.DateField(label='Date of Birth')
	ssn = forms.CharField(label='Social Security Number', max_length=12, required = False, validators=[
            RegexValidator(
                # http://stackoverflow.com/questions/123559/a-comprehensive-regex-for-phone-number-validation
                regex='(^\d{3}-?\d{2}-?\d{4}$|^XXX-XX-XXXX$)',
                message='Invalid ssn',
            ),
        ])
	message = forms.CharField(widget=forms.Textarea, required = False)
  	#credit_score = forms.IntegerField(max_value = 900, min_value = 300)

	def clean_first_name(self):
		cd = self.cleaned_data
		first_name = cd.get('first_name')

		if len(first_name) < 2 :
			raise forms.ValidationError("Please enter at least 2 characters")

		return first_name


class InquiryForm(forms.Form):
	first_name = forms.CharField() # do not validate names
	last_name = forms.CharField() # do not validate names
	email = forms.EmailField()
	phone_number = forms.CharField(label='Phone Number', required=False, validators=[
            RegexValidator(
                # http://stackoverflow.com/questions/123559/a-comprehensive-regex-for-phone-number-validation
                regex='^(?:(?:\+?1\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?$',
                message='Invalid phone number',
            ),
        ])
	comment = forms.CharField(widget=forms.Textarea)
