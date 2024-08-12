#include <stdio.h>

int main() {
	int size = 1001,
	    sum = 1,
	    i;

	for (i = 3; i <= size; i += 2) {
		sum += 2*(2*i*i - 3*i + 3);
	}

	printf("%d\n", sum);
	return 0;
}
