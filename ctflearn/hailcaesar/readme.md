# HailCaesar!

> You might need to write some Python to solve this challenge. Some encryption may be involved. Good Luck!

`file` revealed some stuff, but I decided to checkout  the full `exiftool -a` on the given file as I felt like I was still missing some information. It contained:

* A long base64-encoded introduction, without any practical information on this challenge. It contained some links to other challenges though, which might be interesting if I really don't find anything.

* The following 'flags': `CTFlearn{Hail_Caesar!!!}.CTFlearn{Airplanes_Sometimes_Cause_Inflight_Incidents}.CTFlearn{Flight_32_Leaves_soon_from_gate_126}`. These seem like hints to use a Ceasar cipher, and to try to ASCII characters from 32 until 126? (So, not just the alphabet?)

* Two strings I couldn't make sense of immediately: `2m{y!"%w2'z{&o2UfX~ws%!._s+{ (&@Vwu{ (&@_w%{v{(&0` and `<Y)8><\9Fbu,Hy4ONC}pxP"4st12wn`?@O$6BgQo7i#gtD|s>3lf=`

So I wrote a ceasar cipher in python (see `script.py`) and tried those last two strings as input. I added a stop-condition that checks if `"CTFlearn"` is in the flag. The result is this:

```
┌──(kali㉿kali)-[~/ctflearn/HailCaesar]
└─$ python script.py 
77  [ignore this] CTFlearn{Maximus.Decimus.Meridius}
```

Which is the correct flag! 

*Side note: I'm glad I only checked if the string contained `"CTFlearn"`, not if it started like that, because that would not have worked...*


