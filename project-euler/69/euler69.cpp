#include <iostream>

unsigned int primes[] = { 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 57 };
unsigned long long limit = 1000000;

int main() {
	unsigned long long best = 1;

	for (auto p : primes) {
		if (best >= (limit + p - 1) / p) {
			break;
		}

		best *= p;
	}

	std::cout << best << std::endl;

	return 0;
}
