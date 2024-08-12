# cbm-hackers's jumpjumpjump

> Another simple but tricky crackme... enjoy!!

[Link](https://crackmes.one/crackme/5c1a939633c5d41e58e005d1)

## Solution

![](https://i.imgur.com/XVJVG1r.png)

I opened the given file in IDA and started renaming some variables to clarify what's (what seems to be?) happening:

![](https://i.imgur.com/PMJhPax.png)

So I think I need an input string with length less than or equal to 11, and the characters ASCII values should sum to 1000. Do notice that the newline (enter key) at the end of the input string (which has an ASCII value of 10) is included in this! 

![](https://i.imgur.com/SOpcdTV.png)

Which consists of 9 `d` characters (100), 1 `Z` character (90) and the newline (10).

I won't write a keygen now, as a keygen would be very very similar to the one I just did for the *NomanProdhan's License Checker 0x03* challenge.
