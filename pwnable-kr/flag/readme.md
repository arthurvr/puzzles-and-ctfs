# Toddler's Bottle - flag

> Papa brought me a packed present! let's open it. This is reversing task. all you need is binary.

When I called `strings` on the given file I noticed the following lines:

```
$Info: This file is packed with the UPX executable packer http://upx.sf.net $
$Id: UPX 3.08 Copyright (C) 1996-2011 the UPX Team. All Rights Reserved. $
```

So I downloaded UPX and decompressed the binary using `-d`. After doing that, I openend the file up in IDA.

![](https://i.imgur.com/Lww4zaz.png)

It says the flag must be one of the strcpy arguments. Let's have a look:

![](https://i.imgur.com/Kki1gyK.png)

Which is the flag.
