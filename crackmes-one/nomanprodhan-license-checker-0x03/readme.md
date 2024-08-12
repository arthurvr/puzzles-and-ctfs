# NomanProdhan's License Checker 0x03

> This binary is for beginners to practice reversing. 

> Don't patch the binary, try to create a keygen to solve it.

[Link](https://crackmes.one/crackme/62072dd633c5d46c8bcbfd9b)

## Solution

Looks like we have to pass a numbers-only license as command line argument:

![](https://i.imgur.com/dShBCd4.png)

I opened the program in IDA. Looks like there's a check first to conditionally show the help message:

![](https://i.imgur.com/8B75MiX.png)

This is followed by the following, which looks a lot like a loop:

![](https://i.imgur.com/6v5Ly6q.png)

Looks like it's looping over the characters of the given string, and keeping the sum. Once the string is finished, there's a final comparison: one to check if this sum is 0x32 (50 in decimal). Let's come up with some licenses:

![](https://i.imgur.com/r4Tpraa.png)

## Keygen

I wrote a keygen in `keygen.py`. It adds random digits to a string until the sum is equal to 50.
