# clutter-overflow

> Clutter, clutter everywhere and not a byte to use. `nc mars.picoctf.net 31890`

Given the source code this is quite an easy to recognise, typical buffer overflow. The only difficult part might be computing the right offset, but let's just use a [de Bruijn serquence](https://en.wikipedia.org/wiki/De_Bruijn_sequence) for that.

I usually use gdb-peda for challenges like this, but I wanted to try a pwntools template today. This one is generated using

```
$ pwn template --host mars.picoctf.net --port 31890 ./chall
```

My exploit code are the last lines of the file (`exploit.py`). It uses lots of neat pwntools utility functions -- such as `cyclic_find` to find the offset, `sendlineafter` to inject the payload at the right time, and formatting functions like `p64` so I don't have to worry about endianness. It had been a while since I used pwntools, I'm pleasantly surprised!

![](https://imgur.com/xmiXlP1.png)

Which is the correct flag indeed.
