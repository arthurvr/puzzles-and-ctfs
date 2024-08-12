# crackmes.de's thellurik by svenka

*[Link](https://crackmes.one/crackme/5ab77f5333c5d40ad448c119)*

## Solution 1: Checking out the right code using GDB

Let's check out what the given program does first (on a safe VM, of course):

![](https://i.imgur.com/gmlZxsQ.png)

I put a breakpoint right before the comparison check for the given code, and found the right code on the stack:

![](https://imgur.com/wjiDGTh.png)

This input works indeed:

![](https://i.imgur.com/rwusalO.png)

*This is for input string `d` as username - `d` is ASCII 100 which is often useful for calculating.*

## Solution 2: Writing a keygen

Let's have a look at what the program actually does in IDA:

![](https://i.imgur.com/tIrlyD3.png)

So the `"~1337# ... #~"` part of the code seems hardcoded. The number in between is calculated using some formatting, the length of the name input and the first character of the name input. I was curious if I could reconstruct the number using a calculation myself:

![](https://i.imgur.com/GSYFJWG.png)

Looks like that works! This should enable me to write a complete keygen... Do note that we need to compile to a 32-bit ELF, as the given program is 32-bit too!

I wrote such a keygen in `keygen.c`. Compile it using

```
$ gcc -m32 -o keygen keygen.c
```

And looks like it works:

![](https://imgur.com/C7ssB5i.png)
