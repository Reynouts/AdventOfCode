#Advent of Code: Day 11
import os
import re

with open('{}.txt'.format(os.path.splitext(os.path.basename(__file__))[0]), 'r') as myfile:
	input = myfile.read().split(',')

	x = 0
	y = 0
	z = 0
	maxDistance = 0
	currentDistance = 0
	for i in input:
		if i == "n":
			y -= 1
			x += 1
		elif i == "ne":
			y -= 1
			z += 1
		elif i == "se":
			z += 1
			x -= 1
		elif i == "s":
			y += 1
			x -= 1
		elif i == "sw":
			y += 1
			z -= 1
		elif i == "nw":
			z -= 1
			x += 1
		currentDistance = max(abs(x), abs(y), abs(z))
		
		if (currentDistance > maxDistance):
			maxDistance = currentDistance

	print "Part 1 ::: distance:\t\t" + str(currentDistance)
	print "Part 2 ::: max Distance:\t" + str(maxDistance)
		
		
		
		
		
		
		
"""	

		if 'n' in i:
			y += 1
		if 'e' in i: 
			x += 1
		if 's' in i:
			y -= 1
		if 'w' in i:
			x += 1
		if i == "n":
		elif i == "ne":
		elif i == "se":
		elif i == "s":
		elif i == "sw":
		elif i == "w":
		elif i == "nw":
		

		n  /
nw +--+ ne
  /    \
-+      +-
  \    /
sw +--+ se
  / s  \
	
	
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
	"""