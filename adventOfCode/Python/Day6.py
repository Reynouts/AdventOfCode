#Advent of Code : Day 6

input = "0	5	10	0	11	14	13	4	11	8	8	7	1	4	12	11"
currentBank = map(int,input.split())

cycles = 0
memory = []

# check if currentBank is already in memory (= finished)
while currentBank not in memory:
	# add currentBank to memory and redistribute memory in this cycle (redistribute is take max value and spread it accross the memory bank)
    memory.append(currentBank[:])
    currentMax = max(currentBank)
    currentIndex = currentBank.index(currentMax)
    currentBank[currentIndex] = 0
    while currentMax != 0:
        currentIndex=(currentIndex+1)%len(currentBank)
        currentBank[currentIndex]+=1
        currentMax-=1
    cycles+=1

print cycles # part 1: amount of cycles after duplicate
print len(memory)-memory.index(currentBank) # part 2: amount of cycles inbetween duplicate