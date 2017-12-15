#Advent of Code: Day 15
import time

#compute the next generation. 
#	If picky, it will search for a number which is evenly dividable by modulo
def cycle(generator, multiplier, divider, modulo, picky):
	generator = (generator * multiplier) % divider
	if picky:
		while (generator% modulo != 0):
			generator = (generator * multiplier) % divider
	return generator

#compare last 16 bits of both generations
def compareBinary(genA, genB):
	return (genA & 0xffff) == (genB & 0xffff)

#run part1 or part2
def part(genA, genB, multiA, multiB, divider, cycles, modA=0, modB=0, picky=False):
	count = 0
	for _ in range(cycles):
		if (compareBinary(genA, genB)):
			count += 1
		genA = cycle(genA, multiA, divider, modA, picky)
		genB = cycle(genB, multiB, divider, modB, picky)	
	return count
	
def main():
	#test input
	genA, genB = 65, 8921
	#own input
	genA, genB = 116, 299
	
	#const values
	multiA, multiB = 16807, 48271
	divider = 2147483647
	modA, modB = 4, 8

	# part 1 without being picky and doing 40M cycles
	cycles = 40000000
	count = part(genA, genB, multiA, multiB, divider, cycles)
	print "Part 1: found {} matches".format(count)
	#runs isolated (without part 2) in about 48 seconds
	
	# part 2, being picky and doing 5M cycles
	cycles = 5000000
	count = part(genA, genB, multiA, multiB, divider, cycles, modA, modB, True)
	print "Part 2: found {} matches".format(count)
	#runs isolated (without part 1) in about 33 seconds

if __name__ == "__main__":
	start_time = time.time()
	main()
	print("- %s seconds -" % (time.time() - start_time))