# Toddler's Bottle - blukat

> Sometimes, pwnable is strange...
> hint: if this challenge is hard, you are a skilled player.

This challenge is actually quite fun, it threw me off for a few minutes too. You actually have reading permissions on the `password` file! But beware, its contents is

```
cat: password: Permission denied
```

Entering this as password when the executable asks works for me. *Can't believe I spent 10 minutes on this. I only noticed when putting a gdb-breakpoint right after the executable reads the password file. There, a `cat`-related error didn't make sense: the program does not even use `cat` to open the file.*

