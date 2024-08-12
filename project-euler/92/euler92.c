#include <stdio.h>
#include <math.h>

int squareDigits(int n) {
	int ret = 0;
	while (n != 0) {
		ret += pow(n % 10, 2);
		n /= 10;
	}

	return ret;
}

char chainEnds[10000001];
int chainEnd(int n) {
	if (n == 89 || n == 1) {
		return n;
	}

	if (chainEnds[n]) {
		return chainEnds[n];
	}

	chainEnds[n] = chainEnd(squareDigits(n));
	return chainEnds[n];
}

int main() {
	int count = 0;

	for (int i = 1; i <= 10000000; i++) {
		if (chainEnd(i) == 89) {
			++count;
		}
	}

	printf("%d", count);
	return 0;
}
