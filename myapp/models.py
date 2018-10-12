from django.db import models

class RegionInfo(models.Model):
	zip = models.CharField(max_length = 5)
	county = models.CharField(max_length = 60)
	state_abbreviation = models.CharField(max_length = 2)
	state = models.CharField(max_length = 30)

	def __unicode__(self):
		return self.zip + '/' + self.county

class CountyFees(models.Model):
	county = models.CharField(max_length = 60)
	recording = models.DecimalField(max_digits = 4, decimal_places = 2)
	taxes = models.DecimalField(max_digits = 4, decimal_places = 2)

class Application(models.Model):
	#title = models.CharField(max_length = 60)
	first_name = models.CharField(max_length = 20)
	last_name = models.CharField(max_length = 20)
	#middle_name = models.DecimalField(max_digits = 4, decimal_places = 2)
	#suffix = models.DecimalField(max_digits = 4, decimal_places = 2)
	phone_mobile = models.CharField(max_length = 20, null=True, blank=True)
	phone_home = models.CharField(max_length = 20, null=True, blank=True)
	phone_work = models.CharField(max_length = 20, null=True, blank=True)
	email = models.EmailField(null=True, blank=True)
	ssn = models.CharField(max_length = 11, null=True, blank=True)
	dob = models.DateField(null=True, blank=True)
	credit = models.CharField(max_length = 3, null=True, blank=True)
	loan_type = models.CharField(max_length = 30, null=True, blank=True)
	loan_balance = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
	loan_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
	property_value = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
	#purchase_price = forms.FloatField(widget=forms.TextInput(attrs={'placeholder':'Purchase Price'}))
	zip_code= models.CharField(max_length = 10, null=True, blank=True)
	#cash_out = forms.FloatField()
	property_type = models.CharField(max_length = 30, null=True, blank=True)

	program = models.CharField(max_length = 30, null=True, blank=True)
	down_payment = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
	cash_out = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
	zip_code = models.CharField(max_length = 5, null=True, blank=True)
	county = models.CharField(max_length = 30, null=True, blank=True)
	state = models.CharField(max_length = 30, null=True, blank=True)
	rate = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
	ysp = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
	apr = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
	payment = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
	title_costs_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
	points = models.DecimalField(max_digits=4, decimal_places=3, null=True, blank=True)
	closing_costs = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	investor = models.CharField(max_length = 30, null=True, blank=True)
	comment = models.TextField(null=True, blank=True)

class Inquiry(models.Model):
	#first_name = models.CharField(max_length = 20)
	first_name = models.CharField(max_length = 40)
	last_name = models.CharField(max_length = 20)
	email = models.EmailField(null=True, blank=True)
	phone = models.CharField(max_length = 20, null=True, blank=True)
	comment = models.TextField(null=True, blank=True)
