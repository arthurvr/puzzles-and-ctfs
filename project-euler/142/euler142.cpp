#include <iostream>
#include <cmath>

#define iseven(n) (n % 2 == 0)

using namespace std;

// Say, we call
// A^2 = x + y
// B^2 = x - y
// C^2 = x + z
// D^2 = x - z
// E^2 = y + z
// F^2 = y - z
//
// From this, it follows that:
// x = 1/2 * (A^2 + B^2)
// y = A^2 - x
// z = C^2 - x
//
// where, it is also given that: x > y > z > 0
//
// From this, the following follows:
// * A^2 + B^2 must be even, meaning A and B are either both odd or both even.
// * C must be larger than sqrt(x)
//
// We use this information to loop over possible A, B and C values. To confirm we have found the right solution,
// we check wheter D^2, E^2 and F^2 are indeed squares.

bool isSquare(int i) {
	int sr = sqrt(i);
	return sr * sr == i;
}

int main() {
	for (int A = 3; ; A++) {
		for (int B = iseven(A) ? 2 : 1; B < A; B += 2) {
			int x = (A*A + B*B) / 2;
			int y = A*A - x;
			if (x <= y) {
				break;
			}

			for (int C = (int)sqrt(x) + 1; ; C++) {
				int z = C*C - x;
				if (y <= z) {
					break;
				}

				if (isSquare(x - z) && isSquare(y + z) && isSquare(y - z)) {
					std::cout << x + y + z << std::endl;
					return 0;
				}
			}
		}
	}
}
