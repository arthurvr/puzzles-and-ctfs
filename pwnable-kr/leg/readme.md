# Toddler's Bottle - leg

> Daddy told me I should study arm.
> But I prefer to study my leg!

We should enter whatever the result of `key1() + key2() + key3()` will be. 

* `key1()` returns `pc`, the program counter. In ARM, that's the current instruction plus 8 bytes. (Yes, this confuses me too. It's a legacy thing I think.) That is `0x00008ce4`.

* `key3()` returns the `lr`, the link register. That's the instruction to be returned to after executing `key3()`. I believe that's `0x00008d80`.

* `key2()` is a bit more complicated. In order, I think the following happens:

  - We're adding 1 to the `pc` and storing that in `r6`. I first thought this didn't make any sense - aren't instructions word-aligned? But apparently, in ARM, it does make sense. It tells the processor to execute the next instruction in Thumb mode. [Read the documentation here.](https://developer.arm.com/documentation/dui0473/m/arm-and-thumb-instructions/bx) So `r6` is `0x8d04 + 1`.
  
  - I believe the `.code 16` is also for going in Thumb mode, which is 16-bit. 
  - The pc is now stored in `r3` = `0x8d08`.
  - 4 is added to `r3`: `0x8d0c`.
  - `r0` becomes `r3`: `0x8d0c`.
  - That `r0` is the return value: `0x8d0c`.

That makes the sum we have to find `0x1A770`, that's 108400. That seems to work:

```
/ $ ./leg 
Daddy has very strong arm! : 108400 
Congratz!
My daddy has a lot of ARMv5te muscle!
```

*Figuring out what `key2()` did was quite a pain. As we get the C source code, it might be easier to compile it on an actual ARM machine  (a cloud one?) and check it out using a debugger.*
