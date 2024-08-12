# owo_whats_this's Very Special Number v1

> EM - Very easy mode: patch executable to make all numbers the special number.

> NM - Normal mode: step through with GDB and extract Special Number from memory.

> NM2 - Normal mode 2: Do not look at executable at all. Solve by writing a program to brute force the solution.

> HM - Hard(er) mode: Do not look at memory or brute force. Solve by reverse engineering the assembly instructions.

[Link](https://crackmes.one/crackme/5e6ac90233c5d4439bb2de39)

## Solution 1: Using IDA to find the solution

Looks like the program calls a `generate` function, which generates the solution number:

![](https://imgur.com/4Dp5suc.png)

This uses a `genNum` function, with these arguments:

![](https://i.imgur.com/TivIfkc.png)

The magic numbers are visible in the memory (just click the memory location).  IDA diassembler is so good it almost feels like cheating... Let's find out what `genNum` does now:

![](https://i.imgur.com/AJGH1yC.png)

I then tried to calculate the number myself:

![](https://i.imgur.com/RSdqLye.png)

![](https://i.imgur.com/k09tsMU.png)

## Solution 2: Patching the program

Changing the `jz` instruction in the main-function to a `jnz` makes all numbers pass (well, except the right one that is). That's possible using *Edit > Patch Program > Assemble*. You can save the patched file to a new executable using *Apply patches to input file* in the same menu.

## Solution 3: Using GDB to figure out the solution

I put put a breakpoint right after the `call` for the `generate` function. Then I executed the program and printed the return value (in the `rax` register):

```
gdb-peda$ p/d $rax
$1 = 109713430479
```
