# Bbbbloat

> Reverse engineer this binary.

Perfect time to try to Ghidra: the NSA's reverse engineering tool.

Again it's a program that asks for our favourite number. This seems to be the relevant part of the code:

![](https://i.imgur.com/Ah4kwaG.png)

The number in the if-statement is 549255 in decimal. Indeed, this answer gets us the flag!

