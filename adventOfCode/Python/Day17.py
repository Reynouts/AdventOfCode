#Advent of Code : Day 17

skipInput = 329
currentPosition = 0
myList = []

for i in xrange(2018):
	myList.insert(currentPosition, i)
	currentPosition = (currentPosition + skipInput + 1) % len(myList)

index = myList.index(2017)
print "Part 1 /// the element after 2017 is: {}").format(myList[index+1])

length = 0
lastElement = 0
currentPosition = 0

for i in xrange(50000000):
	if currentPosition == 0:
		lastElement = i
	length += 1
	currentPosition = (currentPosition + skipInput + 1) % length

print "Part 1 /// the element after 0 is: {}").format(lastElement)
