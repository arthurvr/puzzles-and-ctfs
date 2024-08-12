#include <stdio.h>

void main() {
	int x = -2147483648;

	int result1 = 0;
	int result2 = 0;
	int result3 = 0;

	while (result3 != -889275714) {
	    result1 = (x << 3);
	    result2 = x ^ 525024598;
	    result3 = result1 ^ result2;

	    x += 1;
	}

	printf("%d\n", x);
}
