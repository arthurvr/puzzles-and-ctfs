#include <stdio.h>
#include <stdbool.h>
#include <limits.h>

bool isPrime(int x) {
	for (int i = 2; i*i <= x; i++) {
		if (x % i == 0) {
			return false;
		}
	}
	return true;
}

int abs(int x) {
	if (x < 0) {
		return -x;
	}
	return x;
}

int sequenceLength(int a, int b) {
	int n = 0;
	while (isPrime(abs(n*n + a*n + b))) {
		n++;
	}
	return n;
}

int main() {
	int currentSequenceLength;
	int longestSequenceLength = 0;
	int longesta, longestb;

	for (int a = -1000; a <= 1000; a++) {
		for (int b = -1000; b <= 1000; b++) {
			currentSequenceLength = sequenceLength(a, b);

			if (currentSequenceLength > longestSequenceLength) {
				longestSequenceLength = currentSequenceLength;
				longesta = a;
				longestb = b;
			}
		}
	}

	printf("%d\n", longesta * longestb);
	return 0;
}
