# GDB baby steps

## GDB baby step 1

> Can you figure out what is in the `eax` register at the end of the main function? Put your answer in the picoCTF flag format: `picoCTF{n}` where n is the contents of the `eax` register in the decimal number base. If the answer was `0x11` your flag would be `picoCTF{17}`.

I opened the program in GDB and put a breakpoint at the end of `main`. Then ran the program until the breakpoint and printed the `$eax` register. (I used `p/d` to print the register in decimal format.)

![](https://i.imgur.com/gcD1T7v.png)

![](https://imgur.com/5I5WZWx.png)

## GDB baby step 2

> Can you figure out what is in the `eax` register at the end of the main function? Put your answer in the picoCTF flag format: `picoCTF{n}` where n is the contents of the `eax` register in the decimal number base. If the answer was `0x11` your flag would be `picoCTF{17}`.

Did exactly the same (as in the first challenge).

![](https://i.imgur.com/PjIirPw.png)

![](https://i.imgur.com/TyEMkfD.png)

## GDB baby step 3

 > Now for something a little different. `0x2262c96b` is loaded into memory in the main function. Examine byte-wise the memory that the constant is loaded in by using the GDB command `x/4xb` addr. The flag is the four bytes as they are stored in memory. If you find the bytes `0x11 0x22 0x33 0x44` in the memory location, your flag would be: `picoCTF{0x11223344}`.

 Again, I put a breakpoint at the end of main. Then I just used the `x/4xb` command as they asked for. The address we are looking for, `rbp - 0x4`, is visible in the disassembly. 

![](https://i.imgur.com/EMc3RWK.png)

![](https://i.imgur.com/mU9EyoB.png)

## GDB baby step 4

> `main` calls a function that multiplies `eax` by a constant. The flag for this challenge is that constant in decimal base. If the constant you find is `0x1000`, the flag will be `picoCTF{4096}`.

Looks like the multiplication happens in a separate function, so let's have a look at that function:

![](https://imgur.com/0scFVWj.png)

The number in the `imul` (multiplication) call is our answer: `0x3269`. That's `12905` in decimal.
