# caas

> cowsay as a service

this is a typical command injection vulnerability. I added `; ls` to the string to find out about the other files on the file system. Then I added `; cat falg.txt` to make the web page echo the flag.

So the flag is revealed by the reponse on `https://caas.mars.picoctf.net/cowsay/abc;ls;cat%20falg.txt`. (Notice the URL encoding!)

![](https://i.imgur.com/d35yzl7.png)
