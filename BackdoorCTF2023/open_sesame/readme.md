# BackdoorCTF 2023: Open Sesame

An APK file is given (an Android app), which I decompiled using an online tool. The important functions are all in `MainActivity`, and the function and variable names (e.g. `valid_password`) aren't obfuscated. Some simple operations happen on this `valid_password`, which eventually end in a XOR decryption procedure on another hardcoded string.

I recreated those operations in Python:

```python
valid_password = [52, 108, 49, 98, 97, 98, 97]

trim2 = ''.join(map(chr, valid_password))

# This results in "4l1baba"...
# 
# sh4dy is a function that constructs a new string with only digits: it only keeps "41".
sh4dy = "41"

# sl4y3r parses a string as integer and subtracts 1.
sl4y3r = int(sh4dy) - 1

def flag(str, str2):
    return "".join([chr(ord(str[i % len(str)]) ^ ord(str2[i])) for i in range(len(str2))])


print(flag(str(sl4y3r), "U|]rURuoU^PoR_FDMo@X]uBUg"))
```

The resulting flag is:

```
flag{aLiBabA_and_forty_thiEveS}
```
