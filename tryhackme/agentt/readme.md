# TryHackMe: Agent T

> Agent T uncovered this website, which looks innocent enough, but something seems off about how the server responds...

*[Link](https://tryhackme.com/room/agentt)*

I performed an NMAP scan first (the result is in `nmap.log`). Interestingly, a dev (beta) version of PHP is used: PHP 8.1.0-dev. A quick Google search revealed an exploit specifically targetting this version, on [ExploitDB](https://www.exploit-db.com/exploits/49933). 

This exploit worked! I got a reverse shell with root privileges immediately.

```
$ cat /flag.txt
flag{4127d0530abf16d6d23973e3df8dbecb}
```
