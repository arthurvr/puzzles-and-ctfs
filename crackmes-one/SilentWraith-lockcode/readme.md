#  SilentWraith's lockcode

*[Link](https://crackmes.one/crackme/5fda4fa433c5d41f64dee37b)*

## Solution

All code seemed quite comprehendible in the IDA pseudocode view. As usually, I started by renaming some variables and functions to make the program's operations more clear. This is the result. Only these three functions seem relevant.

![](https://i.imgur.com/TXjodcS.png)
![](https://i.imgur.com/BnAT9ct.png)
![](https://i.imgur.com/P5mGQbr.png)

The `val` function seems to calculate the sum of the ASCII values of the characters in the given string. 
There's a password hard-coded, and one from the user input.
The program calculates the `val()` value of both, and shows the success message if `pass_val + 1 - input_val == 1`. This simplifies to `pass_val == input_val`, which is obviously the case when the entered password is equal to the hard-coded one.

Even though I think this program can be trusted, I executed everything on a safe VM. 
Looks like I was right about the valid pass, as I got the success message.

![](https://i.imgur.com/3z81pLU.png)
