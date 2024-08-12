#include <iostream>

#define limit 100000000
bool isPrime[limit + 1];
void sieve() {
	memset(isPrime, true, sizeof(isPrime));

	for (int p = 2; p * p <= limit; p++) {
		if (isPrime[p] == true) {
			for (int i = p * p; i <= limit; i += p) {
				isPrime[i] = false;
			}
		}
	}
}

unsigned int modularInverse(unsigned int a, unsigned int modulo) {
	auto originalModulo = modulo;
	int s = 0;
	int t = 1;

	while (a > 1) {
		auto tmp = modulo;
		auto quotient = a / modulo;
		modulo = a % modulo;
		a = tmp;

		auto tmp2 = s;
		s = t - quotient * s;
		t = tmp2;
	}

	if (t < 0) {
		t += originalModulo;
	}

	return t;
}

unsigned long long facmodprime(unsigned int n, unsigned int modulo)
{
	if (n >= modulo) {
		return 0;
	}

	unsigned long long facmod = modulo - 1;

	for (auto i = modulo - 1; i > n; i--) {
		facmod *= modularInverse(i, modulo);
		facmod %= modulo;
	}

	return facmod;
}

int main()
{
	sieve();

	unsigned long long sum = 0;
	for (unsigned int p = 5; p < limit; p++) {
		if (isPrime[p]) {
			unsigned long long fac5 = facmodprime(p - 5, p);
			unsigned long long fac4 = (fac5 * (p - 4)) % p;
			unsigned long long fac3 = (fac4 * (p - 3)) % p;
			unsigned long long fac2 = (fac3 * (p - 2)) % p;

			sum += (fac2 + fac3 + fac4 + fac5 - 1) % p;
		}
	}

	std::cout << sum << std::endl;
	return 0;
}
