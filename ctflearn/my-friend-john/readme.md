# My Friend John 

> Have you met my friend John?  He's not so scary, even though they call him "The Ripper".

This challenge is clearly about using [John the Ripper](https://github.com/openwall/john).

* As for the first zip file, it's called `use-rockyou.zip` - clearly a reference to the wordlist we should use to brute force its password. To crack a zip file with john the ripper, first use `zip2john`:

```
zip2john use-rockyou.zip > crack1
john crack1 --worldlist=rockyou.txt
```

This reveals the correct password: `kdbs0429`. Note that rockyou is included in Kali Linux by default, in `/usr/share/wordlists/`.

* Inside is another zip file, now with a custom list to use. I used the exact same technique though. For this file the correct password is `1N73rD3N0M1N4710N41`.

* There's another zip file inside, now called `brute-force-pin.zip`. For brute forcing a pin, I like a tool called `fcrackzip` over John the ripper.

```
┌──(kali㉿kali)-[~/ctflearn/my-friend-john]
└─$ fcrackzip -c 1 -l 1-8 -b -u brute-force-pin.zip 

PASSWORD FOUND!!!!: pw == 991337
```

* Inside this last zip file, there's a `flag.txt` containing the flag.
