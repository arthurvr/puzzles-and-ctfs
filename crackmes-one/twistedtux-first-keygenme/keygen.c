#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int func1(int pseudo_length) {
	return (pseudo_length ^ 0x3b) & 0x3f;
}

int func2(char* pseudo, int pseudo_length) {
	int res = 0;
	for (int i = 0; i < pseudo_length; i++) {
		res += pseudo[i];
	}

	return (res ^ 0x4f) & 0x3f;
}

int func3(char* pseudo, int pseudo_length) {
	int res = 1;
	for (int i = 0; i < pseudo_length; i++) {
		res *= pseudo[i];
	}
	return (res ^ 0x55) & 0x3F;
}

int func4(char* pseudo, int pseudo_length) {
	int res = pseudo[0];
	for (int i = 0; i < pseudo_length; i++) {
		if (pseudo[i] > res) {
			res = pseudo[i];
		}
	} 
	srand(res ^ 0xE);
	return rand() & 0x3F;
}

int func5(char* pseudo, int pseudo_length) {
	int res = 0;
	for (int i = 0; i < pseudo_length; i++) {
		res += pseudo[i] * pseudo[i];
	}

	return (res ^ 0xef) & 0x3f;
}

int func6(char pseudo) {
	int res = 0;
	for (int i = 0; i < pseudo; i++) {
		res = rand();
	}
	return (res ^ 0xe5) & 0x3F;
}

int main(int argc, char* argv[]) {
	char hardcoded_str[] = "A-CHRDw87lNS0E9B2TibgpnMVys5XzvtOGJcYLU+4mjW6fxqZeF3Qa1rPhdKIouk";
	char* pseudo = argv[1];
	char clef[7];
	int pseudo_length = strlen(pseudo);

	clef[0] = hardcoded_str[func1(pseudo_length)];
	clef[1] = hardcoded_str[func2(pseudo, pseudo_length)];
	clef[2] = hardcoded_str[func3(pseudo, pseudo_length)];
	clef[3] = hardcoded_str[func4(pseudo, pseudo_length)];
	clef[4] = hardcoded_str[func5(pseudo, pseudo_length)];
	clef[5] = hardcoded_str[func6(pseudo[0])];
	clef[6] = 0;

	printf("Clef: %s\n", clef);
}

