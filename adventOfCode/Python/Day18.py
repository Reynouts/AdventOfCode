#Advent of Code: Day 18
import string
from collections import deque
import os

def Input():
	print os.path.splitext(os.path.basename(__file__))[0]
	with open('{}.txt'.format(os.path.splitext(os.path.basename(__file__))[0]), 'r') as myfile:
		data=myfile.read()
	return data

#execute the instruction on index from input
def executeInstruction(index, variables, queue1, queue2, count):
	instructionLine = instructions[index].split()
	instruction = instructionLine[0]
	variableKey = instructionLine[1]
	waiting = False
	# instructions with third variable
	if len(instructionLine) > 2:
		#if letter, get value from dictionary
		if instructionLine[2].isalpha():
			value = variables[instructionLine[2]]
		else:
			value = int(instructionLine[2])
		# jump in next cycle
		if instruction == "jgz":
			if variableKey.isalpha():
				if variables[variableKey] > 0:
					return value + index, count, waiting
			else:
				if int(variableKey) > 0:
					return value + index, count, waiting
		# all simple operators
		elif instruction == "set":
			variables[variableKey] = value
		elif instruction == "add":
			variables[variableKey] += value
		elif instruction == "mul":
			variables[variableKey] *= value
		elif instruction == "mod":
			variables[variableKey] = variables[variableKey] % value
	#send to queue of other program
	elif instruction == "snd":
		queue2.append(variables[variableKey])
		count += 1
	#receive value out of queue of other program
	elif instruction == "rcv":
		if len(queue1) > 0:
			variables[variableKey] = queue1.popleft()
		else:
			waiting = True
			return index, count, waiting
	return index + 1, count, waiting

#read instructions
instructions = Input().split("\n")

#variables for p0
variables0 = dict.fromkeys(string.ascii_lowercase, 0)
variables0["p"] = 0
queue0 = deque()
count0 = 0
index0 = 0
waiting0 = False

#variables for p1
variables1 = dict.fromkeys(string.ascii_lowercase, 0)
variables1["p"] = 1
queue1 = deque()
count1 =  0
index1 = 0
waiting1 = False

# run until both are waiting (queues are empty and programs are both receiving)
while not waiting0 or not waiting1:
	index0, count0, waiting0 = executeInstruction(index0, variables0, queue0, queue1, count0)
	index1, count1, waiting1 = executeInstruction(index1, variables1, queue1, queue0, count1)

print "Part 2 /// amount of sends for p1: " + str(count1)