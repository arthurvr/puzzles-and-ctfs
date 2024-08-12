# crackinglessons.com's GUI-based CrackMe2

> This GUI-based crackme is a very easy one for absolute newbies. The challenge:

> 1. Find the serial key and enter it in the textbox

> 2.  Patch the file to always show the Congrats message when you click on button Check.

> Written in Visual Studio 2017 win32 API.

Found this challenge on **crackmes.one**: [*Link*](https://crackmes.one/crackme/5e45850133c5d4439bb2db3f)

## Part 1: Finding the serial key

I opened the executable up in IDA. I started by checking the strings (View > Open subviews). I found a success and a failure message, which immediately pointed me to the right part of the source code:

![](https://i.imgur.com/S0TjL8D.png)

![](https://i.imgur.com/p7xpHUv.png)

Checking out the pseudocode view might clarify what this program does exactly. This seems to be the important `strcmp` call:

![](https://i.imgur.com/IsJOijS.png)

That's indeed the valid right there! I got the success message when entering that key.

## Part 2: Patching the executable

This seems to be the decision point between showing the success or the failure message:

![](https://i.imgur.com/N6ZDdlS.png)

I put a breakpoint right before the `jne` call, and changed it to a `jz` call. 

![](https://i.imgur.com/g1cx5dS.png)

That's not the only thing we have to change though.
The `eax` register, which is supposed to be zero when the key is right, is also used after the comparison.
So I put another breakpoint right before it's used, and manually changed it to `0x0`.
And that worked!

![](https://i.imgur.com/2ealKwG.png)
