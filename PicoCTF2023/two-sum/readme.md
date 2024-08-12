# two-sum

> Can you solve this?

> What two positive numbers can make this possible: `n1 > n1 + n2 OR n2 > n1 + n2`?

> Enter them here: `nc saturn.picoctf.net 50548`

The `int` type (usually) overflows at `2147483647`. Check the given code: we should find two integers that don't overflow themselves, but overflow when added together. So I entered something a little less than `2147483647`.

![](https://i.imgur.com/JjdpdqG.png)
 
