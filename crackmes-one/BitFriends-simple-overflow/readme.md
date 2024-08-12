# BitFriends's simple overflow

> This is a very simple crackme. The goal is to get "you are logged in as admin". Patching is not allowed. The solution should contain an exact description, how this works. Have fun!

[Link](https://crackmes.one/crackme/5f05ec3c33c5d42a7c66792b)

## Solution

Looks like them `main` function simply calls another function called `login`:

![](https://i.imgur.com/inBgchb.png)

This login function contains a buffer overflow vulnerability: by inputting more bytes into the prompt, we will start writing over the bytes that make up the `uid` varaible. (Note that I changed the variable names to make the program a bit more readable.) I think this buffer overflow can be used to make `uid` equal to zero.

![](https://i.imgur.com/faqX2ia.png)

Fingers crossed, as there might be some protection mechanisms on:

![](https://i.imgur.com/9qWF5RG.png)

Seems like there isn’t :-)
We need 32 bytes as padding before we start overwriting the `uid` variable. This is due to alignment. I figured this out by checking the address in a debugger, but some trail-and-error would have worked too.

