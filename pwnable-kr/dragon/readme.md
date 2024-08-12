# Rookiss - dragon

> I made a RPG game for my little brother.
>
> But to trick him, I made it impossible to win.
>
> I hope he doesn't get too angry with me :P!

A link is provided to download the executable. I opened it in IDA. I found several things:

* A `SecretLevel` function, accessible by submitting `3` as a hero choice. [Screenshot](https://i.imgur.com/0QpeOJS.png)

* This level contains a `system("/bin/sh")` call, supposedly to target and win this challenge. [Screenshot](https://i.imgur.com/tuRvpbN.png)

* The `strcmp` call checks a password, but the string being compared is too long for the `local_1a` buffer... So setting that buffer correctly won't work.

* There's a use-after-free vulnerability after freeing the dragon objects. The `0x16` bytes of dragon object will be freed, and the memory will be given to the malloc call after that. But the data won't be erased first! This new object we now control contains the pointer to be jumped to at `0x080488bb`. So let's overwrite that one!

See `exploit.py`.
