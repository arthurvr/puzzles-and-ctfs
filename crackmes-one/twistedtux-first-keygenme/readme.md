# TwistedTux' first_keygenme

*[Link](https://crackmes.one/crackme/5ab77f5733c5d40ad448c363)*

## Solution

This crackme seems to be different from many others: there appear to be two input strings. Nothing seems to be displayed whenever we enter something wrong:

![](https://imgur.com/YjXUmIN.png)

(I'm obviously using a safe VM to run this!)

This code block is first, and I think it checks if less than 3 arguments are supplied. In that case, the *"Usage"* message is shown.

![](https://imgur.com/LF4p2Wr.png)

The next block stores the given `pseudo` parameter in `[esp+4]` and `clef` at `[esp+8]`. It calls `strlen` (*string length*) on `clef` and checks if it's equal to 6. If not, we jump to `loc_8048479`, which simply seems to exit the program. If it is equal to 6, we move on.

![](https://imgur.com/ZGH8GAo.png)

Next, there are 6 blocks that look very, very similar. They all look like this, except that they check `clef[0]`, `clef[1]`, `clef[2]`, ... and all call a different function. The first one only takes argument `pseudo_length`, the next ones also take `pseudo`, and the last one only takes `pseudo[0]`. The code blocks loosely translate to this:

```c
char hardcoded_str[] = "A-CHRDw87lNS0E9B2TibgpnMVys5XzvtOGJcYLU+4mjW6fxqZeF3Qa1rPhdKIouk"
char* pseudo = argv[1];
char* clef = argv[2];
int pseudo_length = strlen(pseudo);
int func_1_result = func1(pseudo_length);

if (clef[0] != hardcoded_str[func_1_result]) {
    fail();
}
```

![](https://imgur.com/q1hycbX.png)

So I think I should be able to create the valid code by recreating the `func1` until `func6` functions. I did this in `keygen.c`, and looks like it works:

![](https://imgur.com/gwlx7EM.png)


