import xml.etree.ElementTree as ET

from investors.parkside_adjustments import *
from investors.parkside_programs import *
from common.title import *
from common.calc import *
from common.adjustment_calc import *

class Investor:
	# self is the object itself
	## __init__ is "iniatialize" (constructor)

	def __init__ (self, filename):
		tree = ET.ElementTree(file = filename)
		self.root = tree.getroot()

	def parse (self, matrix, reverse, flip, hundred):

		all_programs = []
		for xy in matrix:
			program_name = []

			# finding the rates and ysps, splitting them, and adding to the program_name array
			for child in self.root.findall(xy):
				for sub_child in child:
					program = sub_child.text.split('\n');
					program_name.append(program)

			# deleting the first and last blank values
			# deleting parentheses
			# outer array
			for i, rates in enumerate(program_name):
				rates.pop()
				rates.pop(0)

				# if ysp's contain parenthesis, remove parenthesis
				# flip values so that negative ysp's are a profit
				if flip==1:
					# inner array, with the actual values
					for j,values in enumerate(rates):

						values = values.replace('(','-')
						values = values.replace(')','')

						values = float(values)

						# flip ysps only
						if i==1:
							values = values*-1

						program_name[i][j] = values
						#print program_name[1][j]

				if hundred==1:
				 	for k,values in enumerate(rates):
				 		#print values
				 		#print i
				 		#print "----"
				 		if i==1:

				 			values = float(values)
				 			values = values - 100
				 			#print program_name[i][k]
				 			program_name[i][k] = values


				# if rates go from higher to lower values
				if reverse==1:
					program_name[i].reverse()

			all_programs.append(program_name)
			self.x = all_programs


	def calcRate(self, prog, loan_amount, property_value, loan_type, property_type, programs, credit_score,  title_costs, total_title_costs, state):
		flag = []
		counter = 0
		# [    [6.6,4.3]  ],    [   [4.3,3.2]    ]  ]
		#x is the index of the outer array (the programID)
		for x in range(len(prog)):
			investor = programs[counter][0]
			margin = programs[counter][2]
			prog_id = programs[counter][7]
			points = calc_points(programs[counter][4], loan_amount)
			closing_costs_borrower = cc (programs[counter][5], total_title_costs)

			try:
				adjustments = investor_adjustment(investor, loan_amount, property_value, credit_score, loan_type, property_type, state, prog_id)
			except:
				adjustments = None # user inputs do not meet guidelines; ltv or credit is out of range

			#adjustments = 999

			try:
				if programs[counter][4] == 0 and programs[counter][5] == 0:
					ysp = margin + adjustments + (total_title_costs/loan_amount * 100)
				elif programs[counter][4] == 1 and programs[counter][5] == 1:
					ysp = 0 + adjustments
				#import pdb; pdb.set_trace()
			except:
				ysp = None
				#ysp = 1

			if ysp != None:

				#y is the index of the inner array (rate is 0, ysp is 1)
				for y in range(1):

					#z is the index of the actual value
					for z in range(len(prog[x][1])): # range is the number of rows in the rate chart
						# if you're not at the highest rate in the chart (haven't reached the end of the array)
						if z+1 < len(prog[x][1]): #comparing the index with the length of the array
							# x is the program, "1" is the ysp, z is the value

							if prog[x][1][z] >= ysp:
								rate = prog[x][0][z] / 100
								inner_flag = []
								inner_flag.append(prog[x][0][z])
								inner_flag.append(prog[x][1][z])
								inner_flag.append(apr(loan_amount, points + total_title_costs, rate, programs[counter][3]))
								inner_flag.append(payment(loan_amount, rate, programs[counter][3]))
								#inner_flag.append(4)
								#inner_flag.append(400)
								inner_flag.append(title_costs)
								inner_flag.append(total_title_costs)
								inner_flag.append(adjustments)
								inner_flag.append(programs[counter][1])
								inner_flag.append(points)
								inner_flag.append(closing_costs_borrower)
								inner_flag.append(investor)
								inner_flag.append(ysp) #test
								flag.append(inner_flag)
								self.rates = flag
								break
							# you've reached the highest rate (last item in the array), so assign it as the rate		
						else:
							rate = prog[x][0][z] / 100
							inner_flag = []
							inner_flag.append(prog[x][0][z])
							inner_flag.append(prog[x][1][z])
							inner_flag.append(apr(loan_amount, points + total_title_costs, rate, programs[counter][3]))
							inner_flag.append(payment(loan_amount, rate, programs[counter][3]))
							#inner_flag.append(4)
							#inner_flag.append(400)
							inner_flag.append(title_costs)
							inner_flag.append(total_title_costs)
							inner_flag.append(adjustments)
							inner_flag.append(programs[counter][1])
							inner_flag.append(points)
							inner_flag.append(closing_costs_borrower)
							inner_flag.append(investor)
							inner_flag.append(ysp) #test
							flag.append(inner_flag)
							self.rates = flag
							break

					counter = counter + 1

		return flag


def calc_points(pts, loan_amount):
	profit = 3000
	if pts == 0:
		points = 0
	else:
		if loan_amount <= 300000:
			points = profit / loan_amount * 100
		else:
			points = 1
	return points


def cc(isCC, total_title_costs):
	if isCC == 0:
		closing_costs_borrower = 0
	else:
		closing_costs_borrower = total_title_costs
	return closing_costs_borrower

