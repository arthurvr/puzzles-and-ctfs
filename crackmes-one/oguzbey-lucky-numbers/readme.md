# oguzbey's Lucky Numbers

> So easy just read assembly code

Found this challenge on **crackemes.one**: [*Link*](https://crackmes.one/crackme/5e567e1d33c5d4439bb2dca0)

## Solution

Looks like we got a 32 bit ELF executable: 

![](https://i.imgur.com/uW2wZTu.png)

Something curious happens when I enter a long number. Seems like only the first two numbers are interesting to the program:

![](https://i.imgur.com/DE1X11v.png)

So the number must be between 10 and 99, easy to brute force... But let's actually reverse the program in IDA, it's too much fun!

To make sense of the program I started by labeling the strings the programs print. 

![](https://i.imgur.com/o3lwXFL.png)

Then onto the application logic... I had to check out what the system calls do exactly. IDA told me it's a read-call but I had to know what was stored where:

![](https://i.imgur.com/6vsKQNa.png)

Looks like the program is reading the two digits, and first subtracting `'0'`. That's converting it to the actual numerical value (instead of the ASCII character). These values are `a1` and `b1`. Then it performs two checks:

![](https://i.imgur.com/IB3RwUM.png)

* It adds them together with carry, and then calls `daa`. That means the result becomes the addition in BCD. [Check this explanation of what these instructions do.](https://www.felixcloutier.com/x86/daa) It checks wheter the result is `0x16` = `0b10110` = BCD for 16. So the possibilities are 79, 97 or 88.

* The second check only involves `b1`: 0x30 is first added to `b1` and then `b1` is compared to `0x38`. That means the last digit must be 8.

That makes 88 the right number!

![](https://i.imgur.com/RYvYoyt.png)
