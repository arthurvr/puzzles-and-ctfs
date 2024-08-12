# Rookiss - rsa calculator

> Pwn this RSA calculator service.
>
> its lame, but it also supports some encryption/decryption.

The help option tells us there are "multiple exploitable vulnerabilities" we can go digging for. I inspected the executable using Ghidra, and indeed I think I noticed multiple vulnerabilities:

1. In both the encrypt and decrypt routine: When asked how long our data is, I can enter a negative number. The loop then stays decrementing this number and doesn't reach zero. I think this would allow me to write outside of the intended buffer.
2. An overflow vulnerability for `g_ebuf`
3. A stack buffer overflow in `RSA_decrypt`.
4. A format string vulnerability at the end of `RSA_decrypt`: we control what's in the decrypted plaintext - so we control what gets passed as format string to `printf`.

There's probably more, but I think this must be enough. The format string vulnerability seemed to most interesting to me. 

I could try to overwrite `exit()` or `help()` to point to shellcode on the stack. That would require predictable stack addresses. I tried something else first: I tried to overwrite the GOT ([*Global Offset Table*](https://en.wikipedia.org/wiki/Global_Offset_Table)) to alter an existing libc-function the program uses. I think this will be the easiest solution, especially if we overwrite `printf`. If we overwrite `printf`, I then immediately control the argument passed to it, because the plaintext decryption result gets passed as an argument. Specifically, I think I will try to overwrite the `printf` offset by `system()`, and then try to call it with argument `/bin/sh`.

I wrote an exploit that does exactly this using pwntools, in `exploit.py`. There's some comments in there to explain the specifics.
