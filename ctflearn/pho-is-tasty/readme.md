# Pho Is Tasty!

> The flag is hidden in the jpeg file. Good Luck! Have some Pho! Solve this challenge before solving my Scope challenge for 100 points.

The flag is in the hexadecimal code. Hexdump is not quite enough (as it doesn't translate ASCII) - use xxd. As the flag is in the start of the file, use `less`.

```
$ xxd pho.jpg | less
```
