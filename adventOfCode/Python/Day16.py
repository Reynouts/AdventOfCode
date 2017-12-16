#Advent of Code : Day 16
import os
import collections

def Input():
	print os.path.splitext(os.path.basename(__file__))[0]
	with open('{}.txt'.format(os.path.splitext(os.path.basename(__file__))[0]), 'r') as myfile:
		data=myfile.read()
	return data

# very inpythonic
def processInput(times, contents):
	for i in xrange(times):	
		for instruction in contents:
			type = instruction[0]
			if type == 's':
				promenade.rotate(int(instruction[1:]))
			elif type == 'x':
				element1 = int(instruction[1:].split('/')[0])
				element2 = int(instruction[1:].split('/')[1])
				promenade[element1], promenade[element2] = promenade[element2], promenade[element1]
			elif type == 'p':
				element1 = list(promenade).index(instruction[1:].split('/')[0])
				element2 = list(promenade).index(instruction[1:].split('/')[1])
				promenade[element1], promenade[element2] = promenade[element2], promenade[element1]
		if promenade == originalPromenade:
			return i+1

#DAY 16
originalPromenade = collections.deque('abcdefghijklmnop')
promenade = collections.deque('abcdefghijklmnop')
# part 1 - do the dance once!
contents = Input().split(",")
processInput(1, contents)
print "This is the promenade of part 1: " + str(promenade)

# part 2 - line up after 1 billion dances
#	reset promenade
promenade = collections.deque('abcdefghijklmnop')
#	search for amount of cycles which leads to the original line up
loop = processInput(10000*1000*100, contents)
#	look for remaining cycles to do and do it
processInput((1000*1000*100)%loop, contents)
print "This is the promenade of part 2: " + str(promenade)
