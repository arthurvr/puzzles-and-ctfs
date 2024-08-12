# Rookiss - syscall

> I made a new system call for Linux kernel.
>
> It converts lowercase letters to upper case letters.
>
> would you like to see the implementation?

I don't have much experience with kernel hacking. I did immediately notice the uncontrolled `out[i] = in[i]` line in the given code, however. It will probably allow us to overwrite any memory we'd like. 
I have no experience with kernel programming either, so I first tried how to legitimately use this custom syscall.

```c
#include <stdio.h>
#define SYS_UPPER			223

int main() {
	char input[] = "abcdef";
	char output[100];

	syscall(SYS_UPPER, input, output);

	printf("%s\n", input);
	printf("%s\n", output);

	return 0;
}
```

```
/tmp/tmp.UGvKAe $ gcc -o demo demo.c
/tmp/tmp.UGvKAe $ ./demo
abcdef
ABCDEF
```

So at least that does what it's supposed to do. Now, how to exploit this? There's a good blog post about kernel privelege escalation [by snyk](https://snyk.io/blog/kernel-privilege-escalation/). Apparently, the call we need to execute to get root priveleges is the following: (These are syscalls too, not simple functions.)

```
commit_creds(prepare_kernel_cred(0));
```

I will attempt to alter the syscall table, to make two other calls that have 1 argument, namely `stime` and `time`, refer to the addresses of `commit_creds` and `prepare_kernel_cred`. Then calling `syscall(25(syscall(13,0))` will hopefully escalate us to root. 

The syscall numbers are in `/usr/include/arm-linux-gnueabihf/asm/unistd.h`.

* `stime` is 25.
* `time` is 13.

The addresses of `prepare_kernel_cred` and `commit_creds` are in `/proc/kallsyms`.

* `commit_creds `is at `0x8003f56c`.
* `prepare_kernel_cred` is at `0x8003f924`.

One problem: the vulnerable syscall won't simply change anything. Bytes between `0x61` and `0x7a` are altered, and the last byte of my `commit_creds` address is such a byte: `0x8003f56c`. We can however, just use `0x8003f560` and add 12 bytes of NOP operations. I used  `\x01\x10\xa0\xe1` as nop here, that's `mov r1,r1`.

I brought this all together in `exploit.c` and added some code to read the flag after the privilege escalation. It works! 😎
