#Advent of Code : Day 12
import os

def Input():
	print os.path.splitext(os.path.basename(__file__))[0]
	with open('{}.txt'.format(os.path.splitext(os.path.basename(__file__))[0]), 'r') as myfile:
		data=myfile.read()
	return data
	
def addConnections(name, parent):
	if name == parent and not connectedTo.get(parent):
		connectedTo[parent] = []
	group = connections.pop(name, None)
	if group:
		for connection in group:
			if connection in connectedTo[parent]:
				"Already added"
			else:
				connectedTo[parent].append(connection)
				addConnections(connection, parent)

contents = Input().split("\n")
connections = {}
connectedTo = {}

#process input
for line in contents:
	split = line.split(' <-> ')
	name = split[0]
	connections[name] = split[1].split(', ')
	
# put all connections in groups (connectedTo)
for connectionName in connections.keys():
	addConnections(connectionName, connectionName)

# length of connectedTo group 0
print "Part 1: " + str(len(connectedTo['0']))

# amount of non zero groups
counter = 0
for group in connectedTo:
	if not connectedTo[group] == []:
		counter += 1
print "Part 2: " + str(counter)
