#Advent of Code : Day 17

skipInput = 329
currentPosition = 0
myList = []

for i in xrange(2018):
	myList.insert(currentPosition, i)
	currentPosition = (currentPosition + skipInput + 1) % len(myList)

index = myList.index(2017)
print "Part 1 /// the element after 2017 is: {}".format(myList[index+1])

length = 0
lastElement = 0
currentPosition = 0

for i in xrange(50000000):
	if currentPosition == 1:
		lastElement = i
	length += 1
	currentPosition = ((currentPosition + skipInput) % length)+1

print "Part 2 /// the element after 0 is: {}".format(lastElement)
