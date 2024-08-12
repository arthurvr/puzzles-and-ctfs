# Modern Gaius Julius Caesar

> One of the easiest and earliest known ciphers but with XXI century twist! Nobody uses Alphabet nowadays right? Why should you when you have your keyboard?

> BUH'tdy,|Bim5y~Bdt76yQ

I googled for `keyboard shift cipher`. There's this really useful site that helps you brute force the amount of places to shift: [dcode.fr ↗️](https://www.dcode.fr/keyboard-shift-cipher).

It's a shift of two characters, on the querty keyboard. That would make the flag `CTFlearn{Cyb3rCae54r}`, which is not correct! Took me a while to figure out, but apparently `~` is not shifted correctly. On that place there should be an underscore! That makes the correct flag `CTFlearn{Cyb3r_Cae54r}`.
