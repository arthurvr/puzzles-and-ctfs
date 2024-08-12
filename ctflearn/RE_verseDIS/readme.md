# RE_verseDIS

> Could you find the hidden password?

I'm usually an IDA guy, but this seems like a nice challenge to try Ghidra. I started a new project and checked out the decompilation first:

![](https://i.imgur.com/fJHJ31e.png)

Again, this seems like some kind of XOR encryption. I won't spend much time in Ghidra any more, and just try to put a breakpoint right after the encryption with gdb. That worked:

![](https://i.imgur.com/T0PeNnD.png)
