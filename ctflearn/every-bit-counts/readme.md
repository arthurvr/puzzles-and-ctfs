# Every Bit Counts

> My colleague is a senior C developer and he had a bad experience in his job assignment. He was developing applications for a real-time embedded operating system named "Buggy OS™". He had to implement workarounds to avoid using the standard C library in some cases. For instance the `memcmp` shouldn't be used to test command-line argument because of obscure reason resulting in some bits were not checked. Instead he implemented its own function to check each bit of the command-line and it was working fine.

> To show case how painful it was, he showed me one of its application implementing his new function, but he forgot the supported command-line parameter.

I openend the given program up using a decompiler (in my case, IDA's decompiler). It contains this very, very long statement to check whether the given command line argument is right.

```c
   (argv[1][28] & 0x20) == 0
&& (argv[1][36] & 0x10) != 0
&& (argv[1][47] & 0x20) != 0
&& (argv[1][32] & 0x20) != 0
&& (argv[1][43] & 4) != 0
&& (argv[1][50] & 0x80) == 0
&& (argv[1][8] & 1) != 0
...
...
...
&& (argv[1][15] & 0x20) != 0
&& (argv[1][11] & 8) == 0
&& (argv[1][24] & 8) != 0
&& (argv[1][14] & 0x40) != 0
&& (argv[1][40] & 8) != 0
&& (argv[1][49] & 1) != 0
&& (argv[1][44] & 1) != 0 
```

In total it's about 400 lines. So, based off this, I tried to write a C program that constructs what the flag should be. Thank god for Vim macros... I did the following:

* Remove every line containing `== 0`, only the non-zero ones are relevant.
* Replace `argv[0]` by a new flag variable I declare myself.
* Remove the parenthesis.
* Remove the `!= 0` part now and put `|=` in between the values to get declarations.
* Print the resulting variable to the screen.

See `solution.c`. And it worked:

![](https://i.imgur.com/Z08aRRq.png)