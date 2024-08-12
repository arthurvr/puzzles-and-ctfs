# File types

> This file was found among some files marked confidential but my pdf reader cannot read it, maybe yours can.

The given file is apparently a [shell archive](https://en.wikipedia.org/wiki/Shar):

![](https://i.imgur.com/4oLLfBI.png)

Extracting such an archive is as simple as executing the script inside of it with `sh`. I obviously read the script before executing it... anything could be inside of there!

![](https://i.imgur.com/cgUj2Gw.png)

The file it contains is an `ar` archive:

![](https://i.imgur.com/sh1tvix.png)

Which we can extract using `ar xv`. Apparently, there's another archive inside! Now a `cpio` archive.

![](https://i.imgur.com/avkiRFV.png)

Which I extract again: (Thank god for `man` pages.)

![](https://i.imgur.com/6k80jjl.png)

A bzip2 file now! Here we go again...

![](https://i.imgur.com/Qdy0TpC.png)

Now this contains a gzip...

![](https://i.imgur.com/NnAF3ET.png)

Now it's an lzip:

![](https://i.imgur.com/GFZ4I5a.png)

And now an lz4 (yes, I'm getting bored of this too)

![](https://i.imgur.com/YLWSUxc.png)

Now an LZMA:

![](https://i.imgur.com/gbQb56z.png)

.. which contains an lzop with an lzip inside...

![](https://i.imgur.com/LiSsXlt.png)

.. Which contains an XZ file, and now I finally get an ASCII text:

![](https://i.imgur.com/zBpl45A.png)

Not the flag yet, but it looks like something hexadecimal. Could again use CyberChef here... or the `xxd` utility.

![](https://i.imgur.com/voajhFJ.png)
