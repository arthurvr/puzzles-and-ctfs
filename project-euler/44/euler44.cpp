// Using this method, we don't need to minimize anything: the closest (j, k) pair found is going to be the first one found.

// S = Pj + Pk = n * (3*n - 1) / 2 = (3*n*n - n) / 2
// D = Pk - Pj = (S - Pj) - Pj = S - 2 * Pj

// Set of pentagonal numbers:
#include <iostream>
#include <set>

using namespace std;

int main() {
	long n = 1;
	long Pj, Pk;
	long S, D;

	std::set <long> ps;

	while (true) {
		n += 1;

		S = (3*n*n - n) / 2;
		ps.insert(S);

		for (long Pj: ps) {
			D = S - 2 * Pj;
			Pk = S - Pj;

			if (ps.contains(Pk) && ps.contains(D)) {
				std::cout << D << std::endl;
				return 0;
			}
		}
	}

	return 1;
}
