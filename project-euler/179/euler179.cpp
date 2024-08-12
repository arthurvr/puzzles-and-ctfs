#include <iostream>
#include <vector>

int main() {
	unsigned int limit = 10000000 + 1;
	unsigned int i, j, result;

	result = 0;
	// Counting the number of divisors
	std::vector<unsigned short> count(limit, 0);
	for (i = 1; i <= limit / 2; i++) {
		for (j = i; j <= limit; j += i) {
			count[j]++;
		}
	}

	// For how many N does N+1 have an equal amount of divisors?
	result = 0;
	for (i = 2; i < limit; i++) {
		result += (count[i] == count[i + 1]);
	}

	std::cout << result << std::endl;

	return 0;
}
