# Jumper

> Hey, I have this simple assembly code.  I need YOUR help. On a particular instruction (address 0x80484e2) I want to know where the call instruction is jumping to (i.e. the address that we are jumping to) (If the user inputs in 'jump'). Specify your answer as a hex number prefixed with '0x', with no leading zeros. Ex. 0x1234. Good luck!

Let me study this section, separately, first. It looks like a loop:

```
80484cc:       8b 45 f0                mov    -0x10(%ebp),%eax
80484cf:       83 c0 05                add    $0x5,%eax
80484d2:       89 45 f0                mov    %eax,-0x10(%ebp)
80484d5:       83 45 f4 01             addl   $0x1,-0xc(%ebp)
80484d9:       83 7d f4 07             cmpl   $0x7,-0xc(%ebp)
80484dd:       7e ed                   jle    80484cc <jump+0x3d>
```

It's adding `0x5`, 8 times. That's equivalent to adding 40.

This part of the code reads 4 characters to a local variable using `fgets`:

```
80484a9:       83 c4 10                add    $0x10,%esp
80484ac:       a1 20 a0 04 08          mov    0x804a020,%eax ; mov eax, 0x804a020
80484b1:       83 ec 04                sub    $0x4,%esp
80484b4:       50                      push   %eax
80484b5:       6a 04                   push   $0x4
80484b7:       8d 45 f0                lea    -0x10(%ebp),%eax
80484ba:       50                      push   %eax
80484bb:       e8 80 fe ff ff          call   8048340 <fgets@plt>
```

The given input `"jump"` translates to `6a 75 6d 70`, but `fgets` only reads 4 bytes with the last one certainly being `0x00`. This is tricky, but the input we need to think about is thus `"jum\x00"`! That's `0x006d756a`.

After adding the 40 that gets us `0x6d7592`. That's the correct flag.
