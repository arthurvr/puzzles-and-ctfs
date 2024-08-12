# Toddler's Bottle - fd

> Mommy! what is a file descriptor in Linux?

Again, I had a look at [the source code](https://i.imgur.com/XH12MVF.png) first.
We can control which file descriptor the program is reading form using the first command line argument.
If we choose `0x1234 = 4660`, it will be reading from `fd = 0`, which is `stdin`. So let's just try that, enter that `LETMEWIN` string and see if it works:

![](https://i.imgur.com/5I3pKzg.png)