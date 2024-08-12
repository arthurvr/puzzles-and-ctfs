module main;
import std.stdio;

bool isLeap(int year) {
	if (year % 100 == 0) {
		return year % 400 == 0;
	}
	return year % 4 == 0;
}

int daysInMonth(int month, int year) {
	switch (month) {
		case 9:
		case 4:
		case 6:
		case 11:
			return 30;
		case 2:
			return isLeap(year) ? 29 : 28;
		default:
			return 31;
	}
}

void main() {
	int count = 0;
	int days;

	// January 1 1901 was a Tuesday.
	int day = 1;

	foreach (int year; 1901..2001)
		foreach (int month; 1..13) {
			if (day == 7) count++;
			day += daysInMonth(month, year) - 1;
			while (day > 7) day -= 7;
		}

	count.writeln;
}
