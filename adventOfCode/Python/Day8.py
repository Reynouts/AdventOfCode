#Advent of Code: Day 8
import os

variables = {}
input = []
maxValue = 0

#parse input file and create variable dictionary.. 
#	replacing variablenames in strings with dictionary ones
with open('{}.txt'.format(os.path.splitext(os.path.basename(__file__))[0]), 'r') as myfile:
	for line in myfile.readlines():
		tmp = line.split(" if ")
		instruction = tmp[0].split(" ")
		if(instruction[0] not in variables):
		   variables[instruction[0]] = 0
		tmp[0] = "variables['" + instruction[0] + "'] " + instruction[1] + " " + instruction[2]		
		condition = tmp[1].split(" ")
		tmp[1] = "variables['" + condition[0] + "'] " + condition[1] + " " + condition[2]
		input.append(tmp)

# the instruction is "parsed", inc and dec are replaced with - and +
# dictionary entry is updated with the evaluation of the instruction
# exec will for example execute: "variables['cr']= variables['cr']-131" for the entry "variables['cr'] dec 131"
def evaluateInstruction(instruction):
	instructionList = instruction.split(" ")
	if instructionList[1] == "inc":
		instructionList[1] = "+"
	else:
		instructionList[1] = "-"
	# "nooooooooo, no exec!! :')"
	exec(instructionList[0] + "=" + ''.join(instructionList))	

#evaluate every line (condition and instruction)
for line in input:
	if(eval(line[1])):
		evaluateInstruction(line[0])
		#part 2
		currentMax = max(variables.values())
		if(currentMax > maxValue):
			maxValue = currentMax

print "Part 1: " + str(max(variables.values()))
print "Part 2: " + str(maxValue)