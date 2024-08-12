# Help Bity

> Bity had the flag for his problem. Unfortunately, his negative friend Noty corrupted it. Help Bity retrieve his flag. He only remembers the first 4 characters of the flag: CTFL.

Converting the given flag to the charcodes gives the following result (thanks CyberChef!):

```
01000010 01010101 01000111 01001101 01100100 01100000 01110011 01101111 01111010 01100011 00110000 01101111 01110011 01111000 01011110 00110000 01110010 01011110 01100000 01110110 01100100 01110010 00110001 01101100 01100100 01111100
```

While "CTFL" is `01000011 01010100 01000110 01001100`. The last bit is always flipped.

I used a simple text editor with macros to flip the bits back:

```
01000011 01010100 01000110 01001100 01100101 01100001 01110010 01101110 01111011 01100010 00110001 01101110 01110010 01111001 01011111 00110001 01110011 01011111 01100001 01110111 01100101 01110011 00110000 01101101 01100101 01111101
```

Which is `CTFLearn{b1nary_1s_awes0me}`.