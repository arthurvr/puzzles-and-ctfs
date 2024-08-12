#include <string.h>
#include <stdio.h>

int main() {
    char* name = "arthur";
    unsigned int v3 = 1;
    for (int i = 0; i < strlen(name); ++i) {
        v3 += name[i];
    }
    unsigned int result = ((431136 * v3 - 3000) / 2 - *name);
    printf("%u\n", result);
}