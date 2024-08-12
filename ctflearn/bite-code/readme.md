# Bite-code

> I dunno what bytecode is. Could you tell me what input of 'checkNum' will return true? The flag is just a 32-bit signed integer as a decimal (nothing else.) 

I don't know Java Bytecode, but the program is quite simple mathematics. I just Googled the name of the given instructions to find out what they do. It seems like the program does a left shift, and two XOR operations. Then there's a condition to stop the program.

It seemed easiest to me to quickly rewrite the calculation in a C program and brute force it. (C because it's easier than starting a Java project and will terminate faster). See `BruteForce.c` :)

That makes the correct flag `CTFlearn{-1352854872}`: a little confusing as I thought the flag would be a decimal ("nothing else")...
