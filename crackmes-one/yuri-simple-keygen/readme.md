# Yuri's Simple Keygen

> 64 bit ELF keygen.
> Understand the algorithm, write a keygen for it

[*Link*](https://crackmes.one/crackme/5c2acb8933c5d46a3882b8d4)

## Solution

Looks like the main program passes `argv[1]` to a function called `checkSerial`.

![](https://i.imgur.com/fwndQK9.png)

That makes sense. Now let me check what that function does exactly. The pseudocode view seems to be easiest to understand:

![](https://i.imgur.com/0jAnDGO.png)

The first comparison is easy: the length of the string should be 16.

For the loop: For even `i`, the `i`th character should be one more than the character before it.

Let's manually try an input string first: I think `2323232323232323` will pass. I used a cloud VM for running the script... not risking anything on my personal computer.

![](https://i.imgur.com/kzltF6S.png)

There's lots of patterns we could let our keygen generate. This keygen works, for example:

<img width="669" alt="image" src="https://user-images.githubusercontent.com/6025224/250141800-39d475cd-1ef1-476e-8a7d-adc1e377065c.png">

