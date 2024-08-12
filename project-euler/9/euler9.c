#include <stdio.h>
#include <math.h>

int main() {
	int a, b;

	for (a = 1; a <= 666; a++) {
		for (b = 1; b <= 333; b++) {
			int c = 1000 - a - b;

			if (a*a + b*b == c*c) {
				printf("%d\n", a*b*c);
			}
		}
	}

	return 0;
}
