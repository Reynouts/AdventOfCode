import os

def Input():
	"Open input file of corresponding day."
	print os.path.splitext(os.path.basename(__file__))[0]
	with open('{}.txt'.format(os.path.splitext(os.path.basename(__file__))[0]), 'r') as myfile:
		data=myfile.read()
	return data

#Day 1: Inverse Captcha
input = Input()
total = 0
shift = len(input)/2 # for first puzzle, shift = 1
for idx, c in enumerate(input):
	if int(c) == int(input[(idx+shift)%len(input)]):
		total = total + int(c)
print total
