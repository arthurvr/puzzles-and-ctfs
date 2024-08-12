# Rookiss - otp

> I made a skeleton interface for one time password authentication system.
>
> I guess there are no mistakes. could you take a look at it?
>
> hint : not a race condition. do not bruteforce.

Looking at the source code, I think a check is missing: what if the file fails to write anything to the `/tmp/randomnumber` file? The file would be empty, and I think entering zero would then get us our flag. However, can we force such a situation?

I started searching around a bit, and then stumbled upon [`ulimit`](https://phoenixnap.com/kb/ulimit-linux-command). I tried limiting the size of files created to 0, but this didn't seem to have the desired effect:

```
otp@pwnable:~$ ulimit -f 0
otp@pwnable:~$ ./otp ''
File size limit exceeded (core dumped)
```

Looks like an error is thrown, and the program is not simply continueing with a zero-sized file. Specifically, a [`SIGXFSZ`](https://en.wikipedia.org/wiki/Signal_(IPC)) (*"singal excess file size"*) is thrown. 

Apparently, if we execute `otp` as a subprocess, we'll be able to [catch and handle](https://stackoverflow.com/questions/38189927/python-how-do-you-catch-unix-signals-received-in-subprocess) this signal... Let's try.

![](https://i.imgur.com/9WeQL9V.png)

Which is the flag!