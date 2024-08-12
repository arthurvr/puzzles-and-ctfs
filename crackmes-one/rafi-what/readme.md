# Rafi’s what

*[Link](https://crackmes.one/crackme/5fd5c44c33c5d424269a1b76)*

## Solution

Looks like we have to [decode a string](https://imgur.com/bo91BeL.png). I used Ghidra to inspect the executable. The code behind `decoder()` is quite straightforward: character per character, its first and second parameter are XORed. That's easily replicable.

![](https://imgur.com/sYWq0Nf.png)

Now, `main` is more confusing. Looks like we always print the `Decode me: ...` message and then exit. The call to `decoder()` is not in the dissasembled code because it's never executed. We have to check the actual assembly to inspect that call.

![](https://imgur.com/OvZ3L33.png)

The three immediate values there seem to express the flag, an equality sign(?), and the key. Using CyberChef:

![](https://i.imgur.com/oWzKHtT.png)
![](https://i.imgur.com/4JmySUX.png)

Note the extra *reverse by character* steps, that are there because of little endianness.

I believe this last value is the flag. Sadly, there doesn't seem to be a way to check this? 
