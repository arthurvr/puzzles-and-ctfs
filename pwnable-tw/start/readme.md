# Start

This first challenge looked like a buffer overflow: entering a string that's too long resulted in a segmentation fault. I used GDB, with [GEF](https://github.com/hugsy/gef) enabled, to exploit this.

Using `checksec` I determined all protections were off, making the exploitation easier.

It looks like quite a classic stack overflow:

![](https://imgur.com/53OJU75.png)

I determined the offset by using a unique pattern: `pattern create` to create the pattern, `pattern search $esp` to find out what's where on the stack. The return pointer was at 24 bytes.

I used pwntools to write an exploit: see `exploit.py`. I could've used any pwntools skeleton or a [gef-extras](https://github.com/hugsy/gef-extras) script too. This got me a shell that could access the flag in `/home/start`.
