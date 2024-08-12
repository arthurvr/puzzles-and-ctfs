# Grotesque - rootkit

> Server admin says he can't access a file even if he has root.
>
> Can you access the file?

Let's again look at the given binary in IDA, and try to figure out what it's doing. Looking at the function names, this looks like a kernel module. That means the functions `initmodule` (and `exitmodule`) are going to be the most interesting.

The variable `sct` is refers to the `SYSTEM_CALL_TABLE`. The module is overwriting some stuff in this system call table. It's providing its own implementation for some of these system calls.

![](https://i.imgur.com/SImqaqF.png)

Now what do these implementations do? Looks like these are all file-related calls, and a check happens for wheter the substring `flag` is in the file name. The calls all fail when `flag` is a substring.

![](https://i.imgur.com/x7nYOV4.png)

So how can we work around this? Apparently, we're logged in as root (uid=0):

```
/ # whoami
whoami: unknown uid 0
```

So we can write our own kernel module, that resets the addresses. I did exactly that in `mymodule.c`. Download the Linux 3.7.1 headers for the right Ubuntu version to compile this. Then call [`insmod`](https://man7.org/linux/man-pages/man8/insmod.8.html) to insert it into the kernel. Now I was able to read the `flag`  file, like any other file. 

It seemed to contain some binary data, and the pwnable-machine was a bit slow, so I extracted its contents using `base64`, so I could work on it locally. According to `file`, it's a gzip:

```
$ base64 -d -i flag.b64 > flag          

$ file flag                            
flag: gzip compressed data, last modified: Fri Jul 24 16:54:31 2015, from Unix, original size modulo 2^32 10240
```

So I unzipped this file and found the flag.
