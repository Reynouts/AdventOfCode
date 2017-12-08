#Advent of Code : Day 7

import os
from collections import Counter

def Input():
	print os.path.splitext(os.path.basename(__file__))[0]
	with open('{}.txt'.format(os.path.splitext(os.path.basename(__file__))[0]), 'r') as myfile:
		data=myfile.read()
	return data

contents = Input().split("\n")
children = {}
weights = {}
totalWeights = {}
balanceFactor = {}

def calculateWeightSubtree(node):
	totalWeight = 0
	for child in children[node]:
		totalWeight += calculateWeightSubtree(child)
	totalWeights[node] = weights[node] + totalWeight
	return totalWeights[node]
	
def calculateBalanceFactor(node):
	if not children[node]:
		balanceFactor[node] = True
		return
	childs = []
	for child in children[node]:
		childs.append(totalWeights[child])
	balanceFactor[node] = (len(set(childs)) == 1)

def pinpointProblem(node):
	if not children[node]:
		"this tree seems balanced"
		return
	factors = [balanceFactor[x] for x in children[node]]
	if (len(set(factors)) == 2):
		"Deeper down the rabbit hole.."
		for child in children[node]:
			if not balanceFactor[child]:
				return pinpointProblem(child)
	else:
		return children[node]

#process input
for line in contents:
	name = line.split()[0]
	weights[name] = int(line.split()[1].strip('()'))
	childs = [x.strip(',') for x in line.split()[3:]]
	children[name] = set(childs)

#find root
for parent in children.keys():
	found = False
	for childs in children.values():
		if parent in childs:
			found = True
			break
	if not found:
		print "The root node is {}".format(parent)
		break
root = parent

#get inbalance
calculateWeightSubtree(root)
for node in children.keys():
	calculateBalanceFactor(node)

#pinpoint problem in the tree
balanceFactorsSet = set(balanceFactor.values())
while(False in balanceFactor.values()): 
# not necessary for this assignment.. only 1 problem and don't need to fix the tree. But fun.
	problemChilds = pinpointProblem(root)
	problemWeights = [totalWeights[x] for x in problemChilds]
	counter = Counter(problemWeights)
	goodWeight = counter.most_common(1)[0][0]
	badWeight = counter.most_common()[-1][0]
	problemChildName = ""
	print "\n\t\t{:8s} {:11s} {:10s}".format("NodeName","totalWeight","WeightNode")
	for child in pinpointProblem(root):
		totalWeight = totalWeights[child]
		weight = weights[child]
		print "\t\t{:>8s} {:11d} {:10d}".format(child,totalWeights[child],weights[child])
		if totalWeight == badWeight:
			problemChildName = child

	print "\n!!Weight of {} should be {}!!".format(problemChildName, weights[problemChildName]-(badWeight-goodWeight))
	print "Fixing.."
	weights[problemChildName] = weights[problemChildName]-(badWeight-goodWeight) #fix inbalance
	
	# recalculate total weights and balance factors
	calculateWeightSubtree(root)
	for node in children.keys():
		calculateBalanceFactor(node)

print "\nThe tree is balanced!"
