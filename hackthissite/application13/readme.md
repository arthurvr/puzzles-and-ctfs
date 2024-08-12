# Application 13

> Find the numbers.

The instructions are quite clear:

![](https://i.imgur.com/9vaJpYT.png)

Indeed, there are a few protections on this file:

![](https://i.imgur.com/T7x2myp.png)

Reversing this file might be harder. The instructions do however hint at a different approach: let's try different numbers and analyse the time taken. I wrote a Python script to do this:

![](https://i.imgur.com/CpRCaIn.png)

Notice how the program is executed multiple times to make the (average) timing more accurate. It worked: 

![](https://i.imgur.com/6Ld2DFe.png)

However, I had to execute this on a separate virtual machine and do nothing else to get the timing to be accurate. That still wasn't perfect, but after a few tries I found the right numbers. Once I  was certain about the first number(s) I just hard-coded them, because executing this script did take a while (~ a few minutes).