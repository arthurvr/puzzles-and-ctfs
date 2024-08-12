# Rookiss - echo1

> Pwn this echo service

Let's check out what the program does (on a safe, empty Kali VM, of course!):

 ```
┌──(kali㉿kali)-[~/Desktop/echo1]
└─$ ./echo1 
hey, what's your name? : arthur

- select echo type -
- 1. : BOF echo
- 2. : FSB echo
- 3. : UAF echo
- 4. : exit
> 1
hello arthur


goodbye arthur
```

Option 1, *BOF echo* seems to be the only option that actually does anything. The others simply print *"not supported"*. So, let's start digging for a buffer overflow, I guess? I opened the executable in IDA.

First I confirmed options 2 and 3 really do nothing, which seems true. Now, `main` and `echo1` seem like the most important functions.

![](https://imgur.com/XsetGEH.png)

As often, the IDA memory location syntax gives away the buffer overflow here. Have a detailed look at `echo1`. It seems to be getting 128 bytes at input, and storing it at `[rbp - 0x20]`. Bingo! This can be used to change the return address. Let’s try to make it jump to some shellcode. However, ASLR is on, making it difficult to predict an addresss where the shellcode will be stored. There’s one other place where we have control over the memory, however. During the execution of `main`, the first 4 bytes on our name gets copied into a global object called `id` at the address `0x6020a0`... Let’s use that address to jump to our shellcode.

I like [this shellcode](http://shell-storm.org/shellcode/files/shellcode-603.html): a very basic call to `execve(“/bin/sh”)`. The complete exploit code is in `exploit.py`, I used pwntools again. It seems to work with both the local executable and the remote one. Simply executing `cat flag` in the reverse shell got me the correct flag.
