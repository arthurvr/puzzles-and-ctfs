# Ramada

> This is a beginners Reversing Challenge. It is build with the optimization level set to 0 so that the assembler is more readable. If you are new to reversing, please remember that to solve Reversing challenges you probably need to know some C/C++, Assembler and also some experience with gdb (the gnu debugger). And maybe Ghidra. So this challenge is a great place to start Reversing, but unfortunately it's only 10 points because it's easier than other reversing challenges. It probably requires more skills than solving a 10 point Forensics problem like RubberDuck. If you solve the challenge you can use the flag to decrypt the sources and see how the challenge is created.

I usually use IDA for reverse engineering, but this seemed like a nice beginner challenge to try Ghidra. I started by opening up the given program and decompiling. The first checks I notice immediately make sense. These check the length of a flag (given as command line argument) and check the first and last characters (`CTFlearn{ ... }`, with a total length of 31).

![](https://i.imgur.com/8DWzglj.png)

Let's try if I'm correct first. I'm confident executing the program on my Kali VM by now, there was nothing really suspicious in there.

![](https://i.imgur.com/fFyUkFn.png)

Yay! Next up, let me checkout the `CheckFlag` function that's called on line 60. The name seems logically chosen: it indeed seems like the function that decides whether the given flag is correct.

![](https://i.imgur.com/R5SGR1M.png)

Notice how the characters in the flag are compared by cubing them, and comparing to whatever's in `data`. I couldn't find the contents of this `data` directly in memory, but then noticed the `InitData` function:

![](https://i.imgur.com/X4p9RHn.png)

Indeed, these numbers are all valid cubes of integers! Seems like I'm right. Do note that the first one is not in order (*_80_4_* should be the last entry, not the first one). I think I can write a simple program that calculates the cube root of these integers, and converts them to ASCII text? I did so in `solution.py` and seems like I'm right:

![](https://imgur.com/zjsPWhB.png)

Yay! That's the flag!
