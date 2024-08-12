# Toddler's Bottle - bof

> Nana told me that buffer overflow is one of the most common software vulnerability. 
Is that true?

We can identify the vulnerability in the source code immediately, especially if we're on the lookout for buffer overflows. The gets-call for `overflowme` clearly allows us to write other memory regions. 

```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
void func(int key){
	char overflowme[32];
	printf("overflow me : ");
	gets(overflowme);	// smash me!
	if(key == 0xcafebabe){
		system("/bin/sh");
	}
	else{
		printf("Nah..\n");
	}
}
int main(int argc, char* argv[]){
	func(0xdeadbeef);
	return 0;
}
```

Now we only have to find out how much we have to overflow the memory to overwrite the `0xdeadbeef`. Let's use gdb and a breakpoint somewhere inside `func` for finding that out. 

![](https://i.imgur.com/07mAJW8.png)

The `0xdeadbeef` value is 52 bytes after the start of the buffer. I used pwntools to actually exploit this. My script is in `exploit.py`.

![](https://imgur.com/9RrfZ9n.png)

