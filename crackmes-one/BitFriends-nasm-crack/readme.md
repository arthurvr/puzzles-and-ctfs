# BitFriends's nasm crack

> Welcome to this easy crackme. Program made with nasm for 64bit intel. Have fun! Can you receive the "Correct!" message?

[Link](https://crackmes.one/crackme/5ea48a1433c5d47611746436)

## Solution

I opened the given program in IDA, it's pretty short:

![](https://i.imgur.com/GiO3o1P.png)

It does the following:

1. A `sys_write` for an `"Enter your password: "` prompt.
2. A `sys_read` call, that stores the result in `buf`.
3. The number 11 is stored in `ecx`, the location of the buffer is stored on `rsi` and the location of a string called `passwd` is stored in `rdi`.
4. `repe cmpsb`: this repeats the `cmpsb` (compare byte) instruction to compare the two strings. It decrements `ecx` for every compared byte until zero.
5. The `jz` instruction: the success message is shown if this comparison succeeds.

So I think entering whatever is at `offset password` should work:

![](https://imgur.com/ZEkG9g4.png)

![](https://imgur.com/AQo3ku1.png)
