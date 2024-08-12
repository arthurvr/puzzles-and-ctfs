# Toddler's Bottle - mistake

> We all make mistakes, let's move on.
>
> (don't take this too seriously, no fancy hacking skill is required at all)
>
> This task is based on real event
>
> Thanks to dhmonkey
>
> hint : operator priority


Again, reading the source code carefully is important. The hint also really helps... Let's focus on this line:

```c
if(fd=open("/home/mistake/password",O_RDONLY,0400) < 0){
```

It does not do what you might think it does. The `<` gets evaluated before the `=`-assignment (= operator priority!). That means `fd` becomes zero.

Making a file handle equal to zero is the same as using standard input `stdin`. So the `read` does not read a file, it reads from user input.

So I think the check will pass if we enter a string, and then enter that same string XOR 1. Let's try:

![](https://i.imgur.com/nEcqull.png)
