# useless

> There's an interesting script in the user's home directory

> The work computer is running SSH. We've been given a script which performs some basic calculations, explore the script and find a flag.

I logged in with SSH using the following command:

```
$ ssh -p 61371 picoplayer@saturn.picoctf.net
```

I read the `useless` file using `cat`:

![](https://i.imgur.com/tIhGVD5.png)

It mentions a manual: this probably refers to the man page.

![](https://i.imgur.com/I1V60wS.png)

Notice the last line contains the flag.
