#include <iostream>

// Advent of Code: Day 15
// Runs in about 1,4 seconds
// Similar implementation in python runs in ~33 seconds

bool compareBinary(size_t genA, size_t genB) {
	return ((genA & 0xffff) == (genB & 0xffff));
}

size_t cycle(size_t gen, size_t multi, size_t divider, size_t mod) {
	gen = (gen * multi) % divider;
	while ((gen % mod) != 0) {
		gen = (gen*multi) % divider;
	}
	return gen;
}

int main() {
	size_t genA{ 116 };
	size_t genB{ 299 };
	const size_t multiA { 16807 };
	const size_t multiB{ 48271 };
	const size_t divider{ 2147483647 };
	const size_t modA{ 4 };
	const size_t modB{ 8 };

	size_t count { 0 };
	for (unsigned int i = 0; i < 5000000; i++) {
		if (compareBinary(genA, genB)) {
			count++;
		}
		genA = cycle(genA, multiA, divider, modA);
		genB = cycle(genB, multiB, divider, modB);
	}
	std::cout << count << std::endl;
	return 0;
}


