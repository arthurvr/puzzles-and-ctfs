# unpackme

> Reverse engineer this binary.

* This time, the `strings` utility doesn't seem to help.
* `strace` and `ltrace` don't help a lot either (= debuggers that can intercept and record library calls, signals, interrupts, system calls, ...).
* The file is called `unpackme-upx`. This seems like a first important hint: it's an executable packed with [UPX](https://upx.github.io/) - let's try to unpack it!
* Unpacking is done using `upx -d` (for *decompress*).
* Again, nothing really useful from `strings` / `strace` / `strings`.
* Okay then... pulling out the big guns: let's open the decompressed program in IDA.

It decompiles to the following code:

```
int __cdecl main(int argc, const char **argv, const char **envp)
{
  char v3; // cl
  int v4; // edx
  int v5; // ecx
  int v6; // r8d
  int v7; // r9d
  int v9; // [rsp+14h] [rbp-3Ch] BYREF
  __int64 v10; // [rsp+18h] [rbp-38h]
  char v11[40]; // [rsp+20h] [rbp-30h] BYREF
  unsigned __int64 v12; // [rsp+48h] [rbp-8h]

  v12 = __readfsqword(0x28u);
  strcpy(v11, "A:4@r%uLFAmk0>b07fH0dfeh3dc6N");
  printf((unsigned int)"What's my favorite number? ", (_DWORD)argv, 1802322246, v3);
  _isoc99_scanf((unsigned int)"%d", (unsigned int)&v9, v4, v5, v6, v7, (char)argv);
  if ( v9 == 754635 )
  {
    v10 = rotate_encrypt(0LL, v11);
    fputs(v10, stdout);
    putchar(10LL);
    free(v10);
  }
  else
  {
    puts("Sorry, that's not it!");
  }
  return 0;
}
```

Looks like a program we can safely execute. When asked for our favorite number, we'll need to tell it `754635`.

* This gets us the flag:

![](https://i.imgur.com/J2KGWWN.png)
