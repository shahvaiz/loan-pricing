from django.shortcuts import render_to_response
from django.template import RequestContext
from myapp.models import CountyFees
from myapp.models import RegionInfo
from myapp.models import Application
from myapp.models import Inquiry
from common.calc import *
from common.title import *
from common.investor import *
from investors.parkside_adjustments import *
from investors.parkside_programs import *
from myapp.forms import ContactForm
from myapp.forms import CalculatorForm
from myapp.forms import InquiryForm
#from myapp.forms import CustomerForm
from myapp.forms import ApplicationForm
from django.http import HttpResponseRedirect
#from django.utils import simplejson
import json
from django.http import HttpResponseRedirect, HttpResponse
import json
import os
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.test import TestCase
#test

def application(request):
	if request.method == 'POST':
		form = ApplicationForm(request.POST)
		abc = None
		abc = request.GET
		if form.is_valid():
			cd = form.cleaned_data
			# insert data into the database

			# application form array is "CD"; loan info array is "abc"

			#user comes to the application directly from the rates page
			if request.GET:
				#import locale
				message = \
				"First Name: " + cd['first_name'] + "\n" + \
				"Last Name: " + cd['last_name'] + "\n" + \
				"SSN: " + cd['ssn'] + "\n"+ \
				"Email: " + cd['email']+ "\n"+ \
				"Phone: " + cd['phone_number'] + "\n"+ \
				"Message: "  + cd['message'] + "\n"+ \
				"Credit: " + abc['credit_score'] + "\n"+ \
				"Loan Type: " + abc['loan_type'] + "\n"+ \
				"Property Value: " + abc['property_value'] + "\n"+ \
				"Zip Code: " + abc['zip_code'] + "\n"+ \
				"Property Type: " + abc['property_type'] + "\n"+ \
				"Program: " + abc['program'] + "\n"+ \
				"Rate: " + abc['rate'] + "\n"+ \
				"APR: " + abc['apr'] + "\n"+ \
				"Points: " + abc['points'] + "\n"+ \
				"Closing Costs to Borrower: " + abc['cc'] + "\n"+ \
				"Investor: " + abc['inv'] + "\n"+ \
				"YSP to BFG: " + abc['y'] + "\n"+ \
				"Closing Costs: " + abc['title'] + "\n"+ \
				"Payment: " + abc['payment'] + "\n"+ \
				"County: " + abc['county'] + "\n"+ \
				"State: " + abc['state'] + "\n"+ \
				"Loan Amount: " + abc['loan_amount']

				loan_balance_message = "\nLoan Balance: $ " + abc['loan_balance']
				cash_out_message = "\nCash Out: $ " + abc['cash_out']
				down_payment_message = "\nDown Payment: $ " + abc['down_payment']

				## no cash out or down payment being inserted into DB
				if abc['loan_type'] == 'refi_rate_term':
					p = Application(first_name = cd['first_name'], last_name = cd['last_name'], email = cd['email'],
					ssn = cd['ssn'],  phone_mobile = cd['phone_number'], comment = cd['message'], credit = abc['credit_score'],
					loan_type = abc['loan_type'], loan_balance = abc['loan_balance'], property_value = abc['property_value'],
					zip_code = abc['zip_code'], property_type = abc['property_type'], program= abc['program'],
					rate = abc['rate'],apr = abc['apr'],points = abc['points'],
					closing_costs = abc['cc'], investor = abc['inv'], ysp = abc['y'], title_costs_total = abc['title'],
					payment = abc['payment'], county = abc['county'], state = abc['state'],
					loan_amount = abc['loan_amount'])

					message = message + loan_balance_message

				## no down payment being inserted into DB
				elif abc['loan_type'] == 'refi_cash_out':
					p = Application(first_name = cd['first_name'], last_name = cd['last_name'], email = cd['email'],
					ssn = cd['ssn'], phone_mobile = cd['phone_number'],comment = cd['message'], credit = abc['credit_score'],
					loan_type = abc['loan_type'], loan_balance = abc['loan_balance'], property_value = abc['property_value'],
					zip_code = abc['zip_code'], property_type = abc['property_type'], program= abc['program'],
					rate = abc['rate'],apr = abc['apr'],points = abc['points'],
					closing_costs = abc['cc'], investor = abc['inv'], ysp = abc['y'], title_costs_total = abc['title'],
					payment = abc['payment'], cash_out = abc['cash_out'], county = abc['county'], state = abc['state'],
					loan_amount = abc['loan_amount'])

					message = message + loan_balance_message
					message = message + cash_out_message

				## no loan balance or cash out inserted into DB
				else:
					p = Application(first_name = cd['first_name'], last_name = cd['last_name'], email = cd['email'],
					ssn = cd['ssn'], phone_mobile = cd['phone_number'],comment = cd['message'], credit = abc['credit_score'],
					loan_type = abc['loan_type'], property_value = abc['property_value'],
					zip_code = abc['zip_code'], property_type = abc['property_type'], program= abc['program'],
					down_payment = abc['down_payment'],rate = abc['rate'],apr = abc['apr'],points = abc['points'],
					closing_costs = abc['cc'], investor = abc['inv'], ysp = abc['y'], title_costs_total = abc['title'],
					payment = abc['payment'], county = abc['county'], state = abc['state'],
					loan_amount = abc['loan_amount'])

					message = message + down_payment_message

				p.save() # insert data into the DB
				send_mail('Website Inquiry', message, 'support@bfgusa.com',
    			['support@bfgusa.com'], fail_silently=False)

				#send_mail('Website Inquiry', message, 'support@bfgusa.com',
    			#['shahvaizhanif@gmail.com', 'shahvaiz@bfgusa.com'], fail_silently=False)

			# user goes to the application form directly (doesn't come from the rates page)
			else:
				message = \
				"First Name: " + cd['first_name'] + "\n" + \
				"Last Name: " + cd['last_name'] + "\n" + \
				"SSN: " + cd['ssn'] + "\n"+ \
				"Phone: " + cd['phone_number'] + "\n" + \
				"Message: " + cd['message'] + "\n" + \
				"Email: " + cd['email']

				p = Application(first_name = cd['first_name'], last_name = cd['last_name'], email = cd['email'],
					ssn = cd['ssn'], phone_mobile = cd['phone_number'],comment = cd['message'])
				p.save() # insert data into the DB
				send_mail('Website Loan Application', message, 'support@bfgusa.com',
    			['support@bfgusa.com'], fail_silently=False)



			return render_to_response('application.html', {'submission': 1})
			#return HttpResponseRedirect('/application/',  {'submission': 1})
				#return HttpResponseRedirect('/application/', {'submission': 1})
				#return render_to_response('application.html')

	else:
		form = ApplicationForm()
		abc = request.GET
	return render_to_response('application.html', {'form': form, 'abc': abc})
	#return render_to_response('application.html', {'form': form, 'abc': abc})

def inquiry_form(request):
	if request.method == 'POST':
		form = InquiryForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			p = Inquiry(first_name = cd['first_name'], last_name = cd['last_name'], email = cd['email'], phone = cd['phone_number'],
					comment = cd['comment'])
			p.save()

			message = \
			"First Name: " + request.POST['first_name'] + "\n" + \
			"Last Name: " + request.POST['last_name'] + "\n" + \
			"Email: " + request.POST['email'] + "\n" + \
			"Phone: " + request.POST['phone_number'] + "\n"+ \
			"Message: " + request.POST['comment']

			send_mail('Website Inquiry', message, 'support@bfgusa.com',
    			['support@bfgusa.com'], fail_silently=False)

			#connection = get_connection(use_tls=True, host='smtp.gmail.com', port=587,username='YourEmail@gmail.com', password='YourPassword')
			#EmailMessage('test', 'test', 'addr@from.com', ['addr@to.com'], connection=connection).send()

			return render_to_response('contact.html',{'submission': 1})

    		#return HttpResponseRedirect('/contact/', {'submission': 1})
    		#return HttpResponseRedirect('/contact/', {'submission': 1})
	else:
		form = InquiryForm()
	return render_to_response('contact.html', {'form': form})

def zip_test(request):

	if request.method == "GET":
		zc = request.GET['zc_check']
		zc_flag = 0
		#zc_result = state_convert(zc);

		if RegionInfo.objects.filter(zip = zc).exists() == True:
			zc_flag = 1

		county = county_convert(zc)
		state = state_convert(zc)

		county = list(county)
		state = list(state)


		#[1, [{"county": "Montgomery"}], [{"state": "maryland"}]]
		#from django.core import serializers
		#county = serializers.serialize('json', 'md')
		#state = serializers.serialize('json', state)

		location_info = [zc_flag, county, state]
		#location_info.append(county)
		# location_info.append(state)

		location_info = json.dumps(location_info)

		#location_info = model_to_dict(location_info)
		#import pdb; pdb.set_trace()


		return HttpResponse(location_info)

def quote(request):

	if request.method == "POST":
		loan_info = ContactForm(request.POST)
		if loan_info.is_valid():
			cd = loan_info.cleaned_data

			#loan_amount = cd['loan_amount']
			property_value = cd['property_value']
			zip_code = cd['zip_code']
			#credit_score = cd['credit_score']
			loan_type = cd['loan_type']
			property_type = cd['property_type']
			loan_balance = cd['loan_balance']
			down_payment = cd['down_payment']
			cash_out = cd['cash_out']

			#import pdb; pdb.set_trace()

			#property_value = property_value.replace(',', '')
			#programID = 000


			# purchase price is an alias for property value
			#if purchase_price > 0:
			#	property_value = purchase_price
			credit_score = float(request.POST['credit_score'])
			loan_amount = float(request.POST['loan_amount']) # loan amount is not in the form; we are deriving this value

			#if loan_type == "refi_rate_term":
			#	loan_balance = loan_amount

			#import pdb; pdb.set_trace()
			county = county_convert(zip_code)
			county = county[0]
			county = county['county']

			#if county == None:
			#	county = "Montgomery"

			state = state_convert(zip_code)
			state = state[0]
			state = state['state']

			#if state is None:
		#		state = "maryland"

			if state == 'maryland' and loan_type == 'purchase':
				case = MD(county)
				title_costs = case.purchase(loan_amount, property_value, county, loan_type, property_type)

			elif state == 'maryland' and loan_type != 'purchase':
				case =  MD(county)
				title_costs = case.refinance(loan_balance, loan_amount, county, loan_type, property_type)

			elif state == 'virginia' and loan_type == 'purchase':
				case =  VA()
				title_costs = case.purchase(loan_amount, property_value, loan_type)

			elif state == 'virginia' and loan_type != 'purchase':
				case =  VA()
				title_costs = case.refinance(loan_amount)

			elif state == 'district of columbia' and loan_type == 'purchase':
				case = DC()
				title_costs = case.purchase(property_value)

			elif state == 'district of columbia' and loan_type != 'purchase':
				case = DC()
				title_costs = case.refinance(property_value)


			# total_title_costs = title_costs[0] + title_costs[1] + title_costs[2] + title_costs[3] + title_costs[4] + title_costs[5] + title_costs[6] + title_costs[7] + title_costs[8]
			total_title_costs = sum(title_costs)

			# first parameter is "reverse": if rates go from high to low, then enter "1" to flip
			# second parameter is "flip": if negative ysp's are profitable, then enter "1" to multiply by -1
			# third parameter is "hundred": if ysps are in the 101.0 format, enter "1" to subtract 100


			ff = os.path.join(os.path.dirname(__file__),  'static/ratesheets/parkside.xml')
			#ff = os.path.join(os.path.dirname(__file__),  'https://console.aws.amazon.com/s3/home?region=us-west-2#&bucket=mystorage-potomac&prefix=ratesheets/parkside.xml')
			parkside = Investor(ff)


			if loan_amount <= 417000:
				parkside.parse(parkside_programs_conforming, 1, 1, 0 )
				programs = parkside_programs_list[0:4] # slice the first 8 rows; use only these programs
			elif loan_amount > 417000 and loan_amount < 625000:
				parkside.parse(parkside_programs_hb, 1, 1, 0 )
				programs = parkside_programs_list[4:10] # slice rows 9 - 12; use only these programs
			else:
				parkside.parse(parkside_programs_jumbo, 1, 1, 0 )
				programs = parkside_programs_list[10:14] # slice rows 13 - 16; use only these programs


			rate_chart = parkside.x
			results = parkside.calcRate(rate_chart, loan_amount, property_value, loan_type, property_type, programs, credit_score, title_costs, total_title_costs, state)

			results = json.dumps(results)


			# a session variable to pass the data to the "Application" view
			# request.session['my_key'] = loan_amount


			# ff = os.path.join(os.path.dirname(__file__),  'static/ratesheets/stearns.xml')
			# stearns = Investor(ff)

			# if loan_amount <= 417000:
			# 	stearns.parse(stearns_programs_conforming, 1, 1, 0 )
			# 	programs = stearns_programs_list[0:8] # slice the first 8 rows; use only these programs
			# elif loan_amount > 417000 and loan_amount < 625000:
			# 	stearns.parse(stearns_programs_hb, 1, 1, 0 )
			# 	programs = stearns_programs_list[8:16] # slice rows 9 - 12; use only these programs
			# else:
			# 	stearns.parse(stearns_programs_jumbo, 1, 1, 0 )
			# 	programs = stearns_programs_list[16:20] # slice rows 13 - 16; use only these programs


			# rate_chart = stearns.x
			# results = stearns.calcRate(rate_chart, loan_amount, property_value, loan_type, property_type, programs, credit_score, title_costs, total_title_costs, state)

			# if loan_amount >= 625000:
			# 	ff = os.path.join(os.path.dirname(__file__),  'static/ratesheets/impac.xml')
			# 	impac = Investor(ff)
			# 	impac.parse(impac_programs, 1, 1, 0 )
			# 	programs = impac_programs_list[:] # slice the whole array
			# 	rate_chart = impac.x
			# 	results2 = impac.calcRate(rate_chart, loan_amount, property_value, loan_type, property_type, programs, credit_score, title_costs, total_title_costs, state)
			# 	results.extend(results2)

			# results = json.dumps(results)

			# Stack Overflow: http://stackoverflow.com/questions/252703/python-append-vs-extend
			# extend:
			# x = [1, 2, 3]
			# x.extend([4, 5])
			# print (x)
			# gives you: [1, 2, 3, 4, 5]

			#import pdb; pdb.set_trace()

		return HttpResponse(results)
	else:
		#calculator_info = CalculatorForm()
		loan_info = ContactForm()
		calc_info = CalculatorForm() # since there are 2 tabs, we need to load both forms on each tab
		return render_to_response('rates.html', {'loan_inputs':loan_info, 'calculator_inputs': calc_info})
		#loan_info = ContactForm()
   		#return render_to_response('rates4.html', {'loan_inputs':loan_info})


def calculator(request):
	if request.method == "POST":

		calc_info = CalculatorForm(request.POST)

		#import pdb; pdb.set_trace()
		#if calc_info.is_valid():
		#	cd = calc_info.cleaned_data

		loan_amount = float(request.POST['loan_amount_calculator'])

		interest_rate = float(request.POST['interest_rate'])
		months = float(request.POST['months'])

		mortgage_details = payment (loan_amount, interest_rate, months)

		#mortgage_details = ammortization (loan_amount, interest_rate, months)
		mortgage_details = json.dumps(mortgage_details)

		#mortgage_details = [100, 200]
		return HttpResponse(mortgage_details)

	else:
		loan_info = CalculatorForm()
		return render_to_response('calculator.html', {'loan_inputs':loan_info})

def programs(request):
	return render_to_response('programs.html',)

def about(request):
   		return render_to_response('about.html',)

def fluid(request):
   		return render_to_response('landing.html',)

def contact(request):
   		return render_to_response('contact.html',)

def investor(request):
   		return render_to_response('investor.html',)

def bankstatement(request):
   		return render_to_response('bankstatement.html',)

def foreignnational(request):
   		return render_to_response('foreignnational.html',)

def noincome(request):
   		return render_to_response('noincome.html',)

def realtors(request):
   		return render_to_response('realtors.html',)
def brokers(request):
   		return render_to_response('brokers.html',)
def purchasenewhome(request):
   		return render_to_response('purchasenewhome.html',)
def homeexperts(request):
   		return render_to_response('homeexperts.html',)
def esign(request):
   		return render_to_response('esign.html',)
def adjustableratemortgage(request):
   		return render_to_response('adjustableratemortgage.html',)
def military(request):
   		return render_to_response('military.html',)
def valoans(request):
   		return render_to_response('valoans.html',)
def easyinvestorloan(request):
   		return render_to_response('easyinvestorloan.html',)
def mortgageloanoptions(request):
   		return render_to_response('mortgageloanoptions.html',)
def sitemap(request):
   		return render_to_response('sitemap.xml',)
