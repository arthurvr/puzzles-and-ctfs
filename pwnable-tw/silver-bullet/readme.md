# Silver Bullet

> Please kill the werewolf with silver bullet!

After playing the given game a bit, it was clear that a bullet could never reach the strength to beat the werewolf.

The given binary was not stripped, so reversing it was pretty easy. I used Ghidra. I think the vulnerability is in the `power_up()` function. It's not very straight forward to notice, but it involves the `strncat(src, dst, N)` call.

![](https://imgur.com/nSEYCsC.png)

Assuming a bullet is stored like this:

```c
struct bullet {
    char[48] description;
    uint power;
}
```

If I enter 48 bytes as input to `power_up()`, then I would overwrite the power of the bullet. I think I can write 48 bytes onto the stack, and use ROP to leak a `libc`-address, and call `system`.
