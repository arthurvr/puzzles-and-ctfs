# GDB Test Drive

> Can you get the flag? Download this binary. Here's the test drive instructions...

Simply following the given instructions gets you the flag.

```
$ chmod +x gdbme
$ gdb gdbme

(gdb) layout asm
(gdb) break *(main+99)
(gdb) run
(gdb) jump *(main+104)
```
