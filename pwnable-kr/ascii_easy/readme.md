# Rookiss: ascii_easy

> We often need to make 'printable-ascii-only' exploit payload.  You wanna try?
> 
> hint : you don't necessarily have to jump at the beggining of a function. try to land anyware.

I saved the given source code in `ascii_easy.c` here. It's quite easy to spot the vulnerable call to `strcpy` inside the source code. Let's check what types of memory protection are enabeld:

```
ascii_easy@pwnable:~$ checksec ascii_easy
[*] '/home/ascii_easy/ascii_easy'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
```

No stack canaries this time :)

There is a check in the source code to make sure we don't enter any non-ASCII characters. That might be a challenge, but I think it's workable. However, I think the main difficulty will be that there is nothing in the source code to read the flag or open a shell.

I downloaded the file that gets mapped to memory, `libc-2.15.so`, and started exploring it a bit. It's libc, as the name suggested already. That's good, as libc contains lots of system calls and code to work with in my exploit. So I went looking for an address to overwrite the return address with, and appropriate argument addresses to pass.  The addresses we need to use will always be the `BASE` from the source code + the offset in the libc file.

Using a combination of `objdump -d`, `strings -t 16`, `grep` and a simple hex editor, I found this in the libc file:

* At `0xb876a` there's a `call` instruction to a `exexve()`.
* At `0x164b58` the path `../sysdeps/unix/sysv/linux/internal_statvfs.c`. That makes `0x164b58` equal to `./sysdeps/unix/sysv/linux/internal_statvfs.c`, which I can use as a relative path within a temporary directory, to symlink `/bin/sh` to and then execute. This will be the first argument to my `execve()` call.
* At `0x6a3a` there's a NULL. I will need a NULL-value, as second and third argument to the `execve` call.

Notice how I carefully selected options where all bytes are within the ASCII range (when added to `BASE`)... that took me a longggg time :/

Using gdb, I then found out that the offset before we start overwriting the return address is equal to 32. I put this all together in `exploit.py`. *Wow, this all took me forever, but it works:*

![](https://imgur.com/cY5JaIF.png)

