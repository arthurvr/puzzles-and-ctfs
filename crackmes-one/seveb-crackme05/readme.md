# seveb’s crackme05

> Welcome to crackme05 reverser!
> Your task is simple, figure out a way to generate valid serials.
> Patching is as expected not allowed. Write a keygen and tell us
> how you solved the crackme.

> Invoke the crackme with the --help or -h flag for additional help.

## Solution

I tried entering a random serial first and got a `Rock 4` error:

![](https://i.imgur.com/oVKMJk4.png)

Now I know that the serial should be 19 characters, but I also have a string I can look for in the IDA *Strings Subview*.

![](https://i.imgur.com/NUvY0X0.png)

As usual, checking out the strings is a fast way to navigate to the relevant code.

### `rock()` and `bomb()`

![](https://i.imgur.com/ueDPaYb.png)

Besides the check for the serial length, this checks if all characters are alphanumeric or the `-` character. Makes sense. If a character is not, `bomb()` gets called.

![](https://i.imgur.com/ucFvQ51.png)

`bomb()` is a slightly misleading function. The first string there looks like a success message, but this is a trap.. it's overwritten later!

### `paper()`

If I pass 18 alphanumeric characters, I now get another error titled "Paper". This seems to correspond to another function that does some checks:

![](https://i.imgur.com/QPzWLrM.png)
![](https://i.imgur.com/Qqkw7Dt.png)

Finding characters that satisfy these simple conditions doesn't seem that difficult with some scripting. Let me first see if there are any more conditions.

### `scissors()`

This looks like some very similar conditions. Again, doesn't look that difficult to write a script that finds satisfying characters.

![](https://i.imgur.com/CyaqvUv.png)

### `cracker()`

There seems to be another function that checks the serial, this one:

![](https://i.imgur.com/FoPWYMB.png)

There are other options, but making those three characters equal to 45 will do the trick. That's the `-` character, which seems logical in a serial code.

### `decraycray()`

This last function seems to do some kind of XOR decryption. However, I don't think it's relevant to the creation of a correct serial. It seems to be used for generating the success message instead.

![](https://i.imgur.com/sfBfN5y.png)

### Keygen

All these conditions are about different characters in the serial so writing a keygen was not very difficult. I wrote it as a recursive function. It starts off with a random string chosen from the characterss allowed by `rock()`, and then does modifications to make it comply with the conditions. If the modifictions are not possible, I just retry with a new random string.

Looks like it works:

![](https://i.imgur.com/RREPgRK.png)
