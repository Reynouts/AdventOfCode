#Advent of Code: Day 9
import os
import re

with open('{}.txt'.format(os.path.splitext(os.path.basename(__file__))[0]), 'r') as myfile:
	garbage = myfile.read()
	garbage = re.sub(r'(!.)', r'', garbage) #remove faulty cleanups
	garbageRe = re.compile(r"(<.*?>)")
	garbageMatches = re.findall(garbageRe, garbage) #store garbage for part2
	garbage = re.sub(garbageRe, '', garbage)#remove self contained garbage
	
	#part 1
	counter = 0
	score = 0
	for character in garbage:
		if character == '{':
			counter += 1
			score += counter
		if character == '}':
			counter -= 1
	print "Part1:\tTotal score of all groups: {:6d}".format(score)
	
	#part 2
	print "Part2:\tAmount of removed garbage: {:6d}".format(sum(len(garbage) for garbage in garbageMatches)-(len(garbageMatches)*2))