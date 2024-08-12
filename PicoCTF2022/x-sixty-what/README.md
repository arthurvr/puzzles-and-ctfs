# x-sixty-what

> Reminder: local exploits may not always work the same way remotely due to differences between machines.

> Overflow x64 code.

> Most problems before this are 32-bit x86. Now we'll consider 64-bit x86 which is a little different! Overflow the buffer and change the return address to the flag function in this program. 

* Again, I'll try to use PEDA and `pattern create` to try to exploit this program. When pasting a long pattern in the input, lots of registers seem overwritten (I checked using GDB). RSP seems to be at offset 72.

* Let's explore the symbol table using `readelf`. We need to find the address of `flag`.

![](https://imgur.com/fYLjhKW.png)

It's `0x401236`.

* Again, I compose an exploit using python. I use pwntools now, which makes handling the addresses a lot easier.

![](https://imgur.com/iSQNSc5.png)

* Locally, this one works!
* However, it does not work on the remote machine. Maybe something is set up differently with relation to the memory layout. Let me try an alternative approach.
* Now I'll try to add one of the return address in between, which is good padding.

* This works!

![](https://imgur.com/KGOTJ3Z.png)

* Just in case: the last hint given by PicoCTF themselves seems useful too: *Jump to the second instruction (the one after the first push) in the flag function, if you're getting mysterious segmentation faults.*
