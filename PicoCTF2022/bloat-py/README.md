# `bloat.py`

> Run this Python program in the same directory as this encrypted flag.

Let's inspect that python file first before running it ;)
It doesn't seem to do anything tricky, but all strings in there seem obfuscated. All strings are written as character-wise combinations of `a`: `a[55]+a[3]+...`. I just copied all strings in a file and deobfuscated them: see `deobfuscate.py`. Now it's easy to see what the password is, and I can run the given script with that password.

![](https://i.imgur.com/rHOrXab.png)
