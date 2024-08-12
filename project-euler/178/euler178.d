module main;
import std.stdio, std.functional;

ulong step(uint pos, uint prev, uint nums, uint max) {
	if (pos == max) {
		if (nums == 1023) {
			return 1UL;
		}

		return 0UL;
	}

	ulong res = 0;

	if (prev < 9) {
		res += memoize!step(pos + 1, prev + 1, nums | 1 << prev + 1, max);
	}

	if (prev > 0) {
		res += memoize!step(pos + 1, prev - 1, nums | 1 << prev - 1, max);
	}

	return res;
}

void main() {
	ulong count = 0;

	foreach (ubyte max; 10..41)
		foreach (ubyte i; 1..10)
			count += step(1, i, 1 << i, max);

	count.writeln;
}
