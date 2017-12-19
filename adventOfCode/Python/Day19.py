#Advent of Code: Day 19
import os

def Input():
	print os.path.splitext(os.path.basename(__file__))[0]
	with open('{}.txt'.format(os.path.splitext(os.path.basename(__file__))[0]), 'r') as myfile:
		data=myfile.read()
	return data

maze = Input().split("\n")
current = (0, maze[0].index('|')) #y,x
heading = (1,0) #start going down
waypoint = '|'
letters = ""
steps = 0

while(waypoint != ' '):
	current = tuple(map(sum,zip(current,heading))) 	#next coordinates
	waypoint = maze[current[0]][current[1]] 		#next symbol in maze
	if waypoint == "+": 							#change heading
		checkpoint = maze[current[0]+heading[1]][current[1]+heading[0]]
		if checkpoint == " ":
			heading = (heading[1]*-1,heading[0]*-1)
		else:
			heading = (heading[1],heading[0])		
	elif waypoint.isalpha():
		letters += waypoint
	steps += 1
	
print "Part 1: solution string is: " + letters
print "Part 2: amount of steps until finished: " + str(steps)