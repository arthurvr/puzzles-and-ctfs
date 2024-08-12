# Toddler's Bottle - passcode

> Mommy told me to make a passcode based login system.
> My initial C code was compiled without any error!
> Well, there was some compiler warning, but who cares about that?

The given source code (which I put in `passcode.c` here) looks legit at first glance. I first thought the challenge would be as simple as entering the right `passcode1` and `passcode2` numbers, but seems like it won't be. The program throws us a segmentation fault after entering the first number. Let's have a closer look at what's happening.

Looks like a `&` (address-of) character is missing on this line:

```c
scanf("%d", passcode1);
```

Which makes us (try to) write at whatever address is in `passcode1`, not in `passcode1` itself. But what will be there? The variable is never initialised with a value, so probably it's just something older on the stack that never gets nulled away... Let's check what's in there using gdb. Don't forget to `source /usr/share/peda/peda.py` inside of the remote, to use PEDA.

I entered `AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA` as name here: 100 characters `A`; the complete name buffer. I entered `1234` (= `0x4d2`) as passcode 1. This error says it all:

![](https://i.imgur.com/Yrm3a6s.png)

Looks like the `scanf` is looking to store `0x4d2` at `0x41414141` (= `AAAA`) now. Logically, that's gonna be the last A characters on the stack, the ones left behind in the undeclared passcode1. That means we can control 1 byte of memory completely, including where to write this byte! 

How to exploit this exactly had me stuck for a while. One byte seems quite limited. Then I thought about the `fflush`-call there in the source code. It doesn't seem appropriate there, as if it wants to be mis-used. I can maybe overwrite what exactly calling `fflush` does?

After searching around a bit, I found out that the part of memory that has the [General Offset Table](https://bottomupcs.sourceforge.net/csbu/x3824.htm) usually has fixed addresses. So what if we overwrite this address?

![](https://i.imgur.com/vgyB6ur.png)

We'll have to overwrite it with another instruction. Maybe the one that calls `system("/bin/cat flag")`? That call is on `0x080485ea`. I will choose one instruction before this, so the argument is still set correctly. So `0x080485e3`.

![](https://i.imgur.com/ywywe37.png)

That makes the complete payload:
* 96 characters of padding, say the `A` character.
* The address we want to overwrite, namely `0x08048430`
* The instruction we want to overwrite it with, namely `0x080485e3`. This should be entered in decimal form (= 134514147)!

Such a payload does not contains any whitespace characters and no null bytes, so I think it should work. (The scanf-call wouldn't allow whitespace in something it believes should be an integer value.) This works:

![](https://i.imgur.com/vdTQmpE.png)
