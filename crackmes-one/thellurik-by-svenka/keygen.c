#include <stdio.h>
#include <string.h>

int main() {
	char input_name[50];

	printf("name: ");
	scanf("%s", input_name);

	int sum = 0;
	for (int i = 0; i < strlen(input_name); i++)
		sum += input_name[i];

	int result_num = ((sum + 3813193) << input_name[0]) ^ 0x1337;

	printf("The right code will be: ~1337#%lu#~", result_num);

}
