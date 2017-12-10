#Advent of Code: Day 10

#input and initialization
input = '157,222,1,2,177,254,0,228,159,140,249,187,255,51,76,30'
lengths =  [ord(x) for x in input]
lengths += [17, 31, 73, 47, 23]
list = range(0, 256)
currentPosition = 0
skipSize = 0

def reverseSublist(begin, end, length):
	swapsToDo = length/2
	while(swapsToDo > 0):
		list[begin], list[end] = list[end], list[begin]
		begin = (begin+1)%len(list)
		end -= 1
		if (end < 0):
			end = len(list)-1
		swapsToDo -= 1

for _ in range(64):
	for length in lengths:
		if length <= len(list):
			reverseSublist(currentPosition, (currentPosition+length-1)%len(list), length)
			currentPosition = (currentPosition + skipSize + length)%len(list)
			skipSize += 1

#part 1 (does not work anymore, with new input and 64 loops)
print str(list[0]) + " and " + str(list[1])
print list[0] * list[1]

#part 2
#	XOR computation
XOR = []
for i in range(16):
	xorValue = 0
	for j in range(16):
		xorValue ^= list[16*i+j]
	XOR.append(xorValue)

#	hex conversion
hexString = ""
for element in XOR:
	print element
	hexi = hex(element)[2:]
	if len(hexi) == 1:
		hexi = "0" + hexi
	hexString += hexi

print hexString
# 2b0c9cc0449507a0db3babd57ad9e8d8