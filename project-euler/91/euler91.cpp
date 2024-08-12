#include <iostream>
#include <math.h>

using namespace std;

int gcd(int a, int b) {
	return b == 0 ? a : gcd(b, a % b);
}

int main() {
	int grid = 50;

	// This accounts for when the points are both on the sides.
	// (All those triangles have 3 possible transformations)
	int result = pow(grid, 2) * 3;

	for (int x = 1; x <= grid; x++) {
		for (int y = 1; y <= grid; y++) {
			int f = gcd(x, y);
			int dx = x / f;
			int dy = y / f;

			result += min(y / dx, (grid - x) / dy) * 2;
		}
	}

	cout << result << endl;
}
