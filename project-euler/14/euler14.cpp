#include <iostream>

using namespace std;

unsigned long getCollatzNumber(unsigned long n) {
	return n % 2 == 0 ? n / 2 : 3*n + 1;
}

unsigned long calculateSteps(unsigned long i) {
	int steps = 1;

	while (i != 1) {
		i = getCollatzNumber(i);
		steps++;
	}

	return steps;
}

int main() {
	unsigned long longest = 0;
	unsigned long longestIndex = 0;

	for (int i = 1; i <= 1000000; i++) {
		int steps = calculateSteps(i);

		if (steps > longest) {
			longest = steps;
			longestIndex = i;
		}
	}

	cout << longestIndex << endl;
}
