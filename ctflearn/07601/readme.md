# 07601

> I think I lost my flag in there. Hopefully, it won't get attacked...

First, there's a fake flag hidden in there:

```
~/c/c/07601 ❯❯❯ strings AGT.png | grep CTF
ABCTF{fooled_ya_dustin}
```

I then used binwalk and found out there's more files hidden in there (and extracted them). This file name looked interesting:

```
~/c/c/07601 ❯❯❯ strings "/Dont Open This.../I Warned You.jpeg" | grep CTF
ABCTF{Du$t1nS_D0jo}1r
```
