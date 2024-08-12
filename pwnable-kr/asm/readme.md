# Toddler's Bottle - asm

> Mommy! I think I know how to make shellcodes

Having a look at the source code, I think the program genuinly does what it says it does: run given x64-code. I had to quickly read up on seccomp on the man page though. I don't think the sandbox should really be an issue: everything we need to open and read the flag file seems to be allowed (lines 19-24).

Writing the shellcode manually would be a pain. Luckily, pwntools has these useful [shellcraft](https://docs.pwntools.com/en/stable/shellcraft.html) utilities for generating shellcode. See `exploit.py` for my code.

```
┌──(kali㉿kali)-[~/Desktop]
└─$ python exploit.py
[+] Connecting to pwnable.kr on port 2222: Done
[*] asm@pwnable.kr:
    Distro    Ubuntu 16.04
    OS:       linux
    Arch:     amd64
    Version:  4.4.179
    ASLR:     Enabled
[+] Connecting to localhost:9026 via SSH to pwnable.kr: Done
Mak1ng_shelLcodE_i5_veRy_eaSy
lease_read_this_file.sorry_the_file_name_is_very_loooooooooooooooooooo
[*] Closed remote connection to localhost:9026 via SSH connection to pwnable.kr
```
