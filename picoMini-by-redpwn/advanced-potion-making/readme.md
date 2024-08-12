# advanced-potion-making

> Ron just found his own copy of advanced potion making, but its been corrupted by some kind of spell. Help him recover it!

* Predictable, but it's worth trying: `file` didn't return anything usefull:

```
$ file advanced-potion-making
advanced-potion-making: data
```

* There's nothing useful when trying `strings` either.

* Let's check the file header using a hex editor. It is

```
89 50 42 11 0d 0a 1a 0a 00 12 13 14 49
```

Which looks a lot like the magic number of a PNG:

```
89 50 4E 47 0D 0A 1A 0A
```

I corrected it to the header of a png file.


* Sadly, I still can't open the file. Having a look at the [PNG specification](https://www.w3.org/TR/PNG-Chunks.html), maybe I have to check the following:

> A valid PNG image must contain an IHDR chunk, one or more IDAT chunks, and an IEND chunk.

But hmm, the bytes themselves do look correct...

* I found a more detailed image of what the header bytes mean. The IHDR length part is not filled in correctly it seems!

![](https://i.stack.imgur.com/hcIIO.png)

I corrected it to `00 00 00 0d` and the file opens correctly!

* The file is all red... usually a good hint to try stegsolve. And indeed, trying the bit planes I found the following:

![](https://i.imgur.com/0GlVNF7.png)

* The flag is indeed `picoCTF{w1z4rdry}`.

