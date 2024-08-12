# Simple Steganography 

> Think the flag is somewhere in there. Would you help me find it? hint-" Steghide Might be Helpfull"

To extract something with steghide, we'll need to find a password first!

```
$ exiftool Minions1.jpeg
...
Keywords                        : myadmin
...
```

This looks like it could be a password. Let's try:

```
$ steghide --extract -sf Minions1.jpeg -p myadmin
```

It contains `AEMAVABGAGwAZQBhAHIAbgB7AHQAaABpAHMAXwBpAHMAXwBmAHUAbgB9`. Could be base64 encoding?

```
$ echo "AEMAVABGAGwAZQBhAHIAbgB7AHQAaABpAHMAXwBpAHMAXwBmAHUAbgB9" | base64 -D
CTFlearn{this_is_fun}
```
