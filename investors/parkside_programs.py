parkside_yield_conforming = 2.75
parkside_yield_hb = 2.75
parkside_yield_jumbo = 2.75

# name, program description, yield, amortization, points, closing costs, name for XML file (Exact mapping needed), program ID code from the rate sheet
parkside_programs_list = [
["parkside", "30 Year Fixed", parkside_yield_conforming, 360, 0, 0,'fixed30', '3510'],
["parkside", "30 Year Fixed", parkside_yield_conforming, 360, 1, 1,'fixed30', '3510'],
["parkside", "15 Year Fixed", parkside_yield_conforming, 180, 0, 0, 'fixed15','3519'],
["parkside", "15 Year Fixed", parkside_yield_conforming, 180, 1, 1,'fixed15','3519' ],
["parkside", "30 Year Fixed", parkside_yield_hb, 360, 0, 0,'fixed30hb', '3531'],
["parkside", "30 Year Fixed", parkside_yield_hb, 360, 1, 1,'fixed30hb', '3531'],
["parkside", "15 Year Fixed", parkside_yield_hb, 180, 0, 0, 'fixed15hb','3532'],
["parkside", "15 Year Fixed", parkside_yield_hb, 180, 1, 1,'fixed15hb','3532' ],
["parkside", "5/1 ARM", parkside_yield_hb, 360, 0, 0, 'arm51hb','3535'],
["parkside", "5/1 ARM", parkside_yield_hb, 360, 1, 1,'arm51hb','3535' ],
["parkside", "Jumbo 30 Year Fixed", parkside_yield_jumbo, 360, 0, 0, 'jumbo30','5521'],
["parkside", "Jumbo 30 Year Fixed", parkside_yield_jumbo, 360, 1, 1,'jumbo30','5521' ],
["parkside", "Jumbo 5/1 ARM", parkside_yield_jumbo, 180, 0, 0, 'jumbo51','5505'],
["parkside", "Jumbo 5/1 ARM", parkside_yield_jumbo, 180, 1, 1,'jumbo51','5505' ],
]

# for the XML file mapping
parkside_programs_conforming  = [
parkside_programs_list[0][6],
parkside_programs_list[1][6],
parkside_programs_list[2][6],
parkside_programs_list[3][6],
]

parkside_programs_hb  = [
parkside_programs_list[4][6],
parkside_programs_list[5][6],
parkside_programs_list[6][6],
parkside_programs_list[7][6],
parkside_programs_list[8][6],
parkside_programs_list[9][6],
]

parkside_programs_jumbo = [
parkside_programs_list[10][6],
parkside_programs_list[11][6],
parkside_programs_list[12][6],
parkside_programs_list[13][6],
]
