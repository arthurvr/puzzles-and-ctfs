# Rookiss - brain fuck

> I made a simple brain-fuck language emulation program written in C. 
>
> The [ ] commands are not implemented yet. However the rest functionality seems working fine. 
>
> Find a bug and exploit it to get a shell. 
>
> Download : `http://pwnable.kr/bin/bf`, `http://pwnable.kr/bin/bf_libc.so`
> 
> Running at : nc pwnable.kr 9001

This refers to the [brainfuck](https://en.wikipedia.org/wiki/Brainfuck) esoteric programming language. At the start of the program, an infintely large array is created. Then, the language has the following operators.

* `>`, equivalent to `++ptr`.
* `<`, equivalent to `--ptr`.
* `+`, equivalent to `++*ptr`.
* `-`, equivalent to `--*ptr`.
* `.`, equivalent to `putchar(*ptr)`.
* `,`, equivalent to `*ptr = getchar()`.
* `[` and `]`, but those are not implemented.

So very much inspired by a turing machine. Of course, I already have some suspicions, but let's check out the implementation in IDA. It's pretty much as expected, I added some screenshots on this [imgur](https://imgur.com/a/Tw6mynq). Let's already write down `p = &tape = 0x0804A0A0` (which is in `.bss`). I think we have a lot of control over the this tape pointer, there don't seem to be much checks in place. However, do note the non-executable stack (NX) and stack canaries:

```
$ checksec bf
[*] '/Users/arthur/code/pwnable-kr-writeups/brain-fuck/bf'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      No PIE (0x8048000)
```

This is probably a good use case for [return-oriented programming](https://en.wikipedia.org/wiki/Return-oriented_programming). We will alter what the program does by modifying the available functions, and try to work our way to a `system("/bin/bash")` call. The argument string we can get there using the program input. However, instead of using a tool like ROPgadget, we'll write gadgets in the brainfuck language.

What I will try to do, concretely:

1. Overwrite `fgets` with `system`.
2. Overwrite `memset` with `fgets`.
3. Overwrite `putchar` with `main`. This will make us re-enter main later, executing everything.
4. Leak the `libc` address, to calculate the right address of `system` and `gets`.
5. Use those address and pass `"/bin/bash"` as argument.

I did this in `exploit.py` and it got me a shell :)

*I spent a lottt of time debugging my exploit and it turned out to be a typo in an address I typed from IDA... Lesson learned: use pwntools `ELF()` and refer to the symbol names instead 🥲*
