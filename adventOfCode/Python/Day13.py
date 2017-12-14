#Advent of Code : Day 12
import os

def Input():
	print os.path.splitext(os.path.basename(__file__))[0]
	with open('{}.txt'.format(os.path.splitext(os.path.basename(__file__))[0]), 'r') as myfile:
		data=myfile.read()
	return data

# very inpythonic
def processInput():
	ranges = {}
	max = 0
	contents = Input().split("\n")
	for line in contents:
		split = line.split(': ')
		depth = int(split[0])
		ranges[depth] = int(split[1])
		if depth > max:
			max = depth
	return ranges, max

def checkState(i, steps):
	global severity #whoops.. sorry
	# 2*n - 2
	if  steps%((2*ranges[i])-2) == 0:
		severity += (i * ranges[i])
		return False
	return True
			
def routeFree(delay, part):
	steps = delay
	for i in range(max+1):
		if i in ranges:
			if not checkState(i, steps):
				if(part == 2):
					return False
		steps += 1
	return True

# read input and put it in some dictionary "ranges"
ranges, max = processInput()
severity = 0

# part 1 - find severity for running through without delay
routeFree(0, 1)
print "Part 1 --- Severity of this walk:\n {}".format(severity)

# part 2
# find delay which results in no severity
delay = 0
while(not routeFree(delay, 2)):
	delay += 1
print "Part 2 --- Amount of delay needed to have no severity:\n {}".format(delay)