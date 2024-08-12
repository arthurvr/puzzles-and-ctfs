# Picker IV

> Can you figure out how this program works to get the flag?

Not a Python program this time. This is a C program that jumps to an address we input. There is a `win()` function again, that prints the flag. I just used a debugging/disassembly tool (IDA) to figure out the address of this `win()` function.

```
$ nc saturn.picoctf.net 57407 
Enter the address in hex to jump to, excluding '0x': 0040129e
You input 0x40129e
You won!
picoCTF{n3v3r_jump_t0_u53r_5uppl13d_4ddr35535_b8de1af4}
```
