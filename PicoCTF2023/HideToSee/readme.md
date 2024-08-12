# HideToSee

> How about some hide and seek heh? Look at this image here.

The given image represents an [Atbash cipher](https://en.wikipedia.org/wiki/Atbash): a simple substitution cipher. But now I also needed a ciphertext to decipher... I tried `strings` and `binwalk` first, but found an `encrypted.txt` file using `steghide`. It contained the following:

```
krxlXGU{zgyzhs_xizxp_zx751vx6}
```

An atbash cipher (or any substitution cipher really) is easy to implement, but [CyberChef](https://cyberchef.org) has an Atbash cipher recipe built in too. I got the following result:

```
picoCTF{atbash_crack_ac751ec6}
```
