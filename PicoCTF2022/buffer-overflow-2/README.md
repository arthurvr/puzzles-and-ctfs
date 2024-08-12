# Buffer Overflow 2

> This time you'll need to control the arguments to the function you return to!

Inspecting the source code, it looks like we will have to overwrite the arguments indeed. See line 20 and 22:

```c
  if (arg1 != 0xCAFEF00D)
    return;
  if (arg2 != 0xF00DF00D)
    return;
```

I checked the address of `win` using `objdump -D` [again](../buffer-overflow-1): `0x08049296`.

I used the same `pattern` technique to find the offset: 112 characters. Now I also used GDB and a breakpoint to find the location of the arguments. Turns out I need another four bytes of offset between the address and the arguments.

And I again used Python again to create the payload, see `script.py`.

![](https://i.imgur.com/bM7ZQZD.png)
