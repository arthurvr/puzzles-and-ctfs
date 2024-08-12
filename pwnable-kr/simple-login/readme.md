# Rookiss - simple login

> Can you get authentication from this server?

I checked the assembly code (and diassembled source code) using IDA. These two functions are the most important it seems, `main` and `auth`.
[Screenshot ↗️](https://i.imgur.com/7fwaU3x.png)

The way IDA represents the memory locations, it's relatively easy to spot a memory overflow vulnerability. Notice how the input is allowed to be 12 bytes long, but is copied to a location at `[ebp - 8]` (see `auth()`). That makes it possible to overwrite EBP.
The program also makes it relatively easy to exploit this, because there is already [a line of code](https://i.imgur.com/LZbXZ1m.png)
 in `correct()` that opens a `/bin/sh` shell. I constructed a payload like this: 

```py
import base64

payload = b"ABCD"
payload += b"\x84\x92\x04\x08"    # The call to system("/bin/sh")
payload += b"\x40\xeb\x11\x08"    # Changing the stack to .bss:0x0811EB40 (= the block starting symbol)

print(base64.b64encode(payload).decode('utf-8'))
```

Notice how it's actually easier to construct a payload when the input is taken as Base64: there is no need to worry anymore about how to input special characters (null bytes, newlines, ...) to the program using stdin.

Now, once I have the reverse shell, I only have to `cat` the flag file.
![](https://i.imgur.com/aSIsC2M.png)
