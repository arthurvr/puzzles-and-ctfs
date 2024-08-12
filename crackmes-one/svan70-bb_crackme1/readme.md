# svan70's bb_crackme1

https://crackmes.one/crackme/5ab77f5e33c5d40ad448c734

Looks like a typical crackme: we have to find a valid serial code.

![](https://i.imgur.com/v1tINMP.png)

I used IDA, but any reversing tool or good debugger will do. I do like IDAs way to switch between assembly, graph view and pseudocode though. Finding the relevant code was easy using the *[Strings](https://i.imgur.com/PCBZRBp.png) subview*.

## Finding the right serial format

There's some windows API code and some dialog boxes for the *About*-description. After that, first interesting code block is this one:

![](https://i.imgur.com/7W7VgVs.png)

I had to check out the documentation of this `__isctype` function. The type `4`  here refers to an integer. This loop checks if every character is a digit. Right after that there's code that expects a `-` character called the "Delimiter", and this code is repeated 3 times. So it looks like the serial has to be in the format `1234-1234-1234` (the last block doesn't check for a `-` anymore).

Indeed, right after this, two other calls make sense:

* `strtok`: splits the serial, given the right delimiter again.
* `strtoul`: convers the first token to an actual integer.

## Square-and-multiply calculation

After reading the number using `strtoul` another function seems to be called.

![](https://i.imgur.com/HyLPT29.png)

The number itself is a parameter, and so is the constant `0xF2CEA371` (4073628529). The function itself looks very repetitive, but it probably wasn't written that way. The compiler is probably applying *loop unwinding*.

![](https://i.imgur.com/eif2sqS.png)

This looks like the *square-and-multiply* algorithm: an efficient way to calculating large powers in a semigroup (*"modulo n"*). The inner loop is repeated 16 times so this function will calculate

> a1^(2^16 + 1) mod a2 = a1^65537 mod a2
> where a2 = 4073628529

This makes me think about the mathematics behind RSA! But with a small modulo and this exponent, that should be crackable in any case.

## Maths!

This square-and-multiply routine is used on all three numbers on the serial, and the results are compared to these constants:

![](https://i.imgur.com/5EWdLSy.png)

So we have to solve this system to find the serial `c1-c2-c3`:

```
c1 ^ 65537 mod 4073628529 = 0x72838e4
c2 ^ 65537 mod 4073628529 = 0x6dc2b9d4
c3 ^ 65537 mod 4073628529 = 0x3ae1ed1e
```

The modulo is easy to [factor](https://i.imgur.com/b40im2e.png) as `47051 x 86579`, which makes these solutions easy to find. Remember RSA: just calculate the totient and then `d` to find these solutions. This is `d`:

![](https://i.imgur.com/cK3N9Zb.png)

And now calculate the solutions this way:

![](https://i.imgur.com/zlZ8nlr.png)

And make the same calculation for the second and third number in the serial. This makes for `580276954-895936478-64598366`, which works! Yay!

![](https://i.imgur.com/okMF0h5.png)
