# Reykjavik

> Good beginning reversing challenge - jump into gdb and start looking for the flag.

I used gdb (+ peda) to find the flag:

1. Open gdb on the given program.
2. Use `start` to bring the program to the point right before starting `main`.
3. I call `disas` to show the program instructions.
4. As the program seems to compare a given string to a known one, I put a breakpoint before the `strcmp` call.
5. Then I run the program with a dummy argument: `run CTFexample`.
6. Yay! My breakpoint must've been on the right point. Check the stack for the right flag:

![](https://imgur.com/qmcFLUN.png)
