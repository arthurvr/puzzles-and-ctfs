# Lafarge crackme v0.2

[Link](https://crackmes.one/crackme/5ab77f5633c5d40ad448c2f0)

## Solution

Let's check out what the program does first. (On a VM, of course.) Looks like the usual username + license code, in a GUI.

![](https://i.imgur.com/LND6Elg.png)

That said, looks like it's quite old yet. Also, notice it's 32-bit. Most tooling will figure this out by itself, but some have separate 32-bit and 64-bit versions.

![](https://i.imgur.com/HrE2Kr2.png)

By looking at the interesting strings I found the all-important `cmp` call in `x32dbg`. With a breakpoint I can now easily figure out what the right license key for a given username is:

![](https://i.imgur.com/0t0hhNB.png)

![](https://i.imgur.com/2tshymg.png)

This was the result for username `arthur` -- and that seems right indeed:

![](https://i.imgur.com/CfjEt6j.png)

### Writing a keygen

Now, I openend the program up in IDA. Again, I used the *Strings* subview to figure out where the interesting code is: 

[](https://i.imgur.com/70KuluW.png)

The most readable view to me is the *Pseudocode* one here -- with disassembled code.
Renaming all variables to clarify what's happening helps a lot:

![](https://i.imgur.com/lmyjZ94.png)

Now I replicated this computation in Python, in `keygen.py`. The script asks for the username and generates the right license key, very much like the instructions themselves do.
