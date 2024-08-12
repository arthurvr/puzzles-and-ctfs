# breadth

> Surely this is what people mean when they say "horizontal scaling," right?

> Our operatives managed to exfiltrate an in-development version of this challenge, where the function with the real flag had a mistake in it. Can you help us get the flag?

I tried simply using `strings` on the given files first, but apparently there's lots of false flags in the binary.

Sounds like the differences between the given `breadth.v2` and `breadth.v1` files are going to be interesting though. Let's check them out using `cmp`:

![](https://i.imgur.com/qymy34L.png)

Especially that second block, starting at `610380` = `0x9504c`. Let's find out what's on this address using IDA: I just jumped to this address and this function showed up.

![](https://imgur.com/hwVC5bB.png)

Just need to click the flag now to jump to the complete one in memory:

![](https://imgur.com/KuT8cFd.png)

This is indeed the correct flag :)
