# Dreammm's Easy - Medium (My first СrackMe)

> All you have to do - enter password.

> Good luck, and Have A Nice Day :)

Found on **crackmes.one**: [Link](https://crackmes.one/crackme/5ec0207b33c5d449d91ae508)

## Solution

IDA immediately dropped us into the main procedure. Looks like one of the final comparisons is a comparison which decides wheter to show the success message. I renamed the memory locations and added some comments to make clear what is happening:

![](https://i.imgur.com/ZEKj6MA.png)

Now for the `cmp` call:

* The first argument is the memory location the user input is stored at.
* The first argument is EAX, which became `988650 - 301296 + 1702271 = 2389625`.

So `2389625` is the password.