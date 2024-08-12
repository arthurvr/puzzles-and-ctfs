# PIN

> Can you crack my pin?

My go-to application for reverse engineering is IDA. The free version will do!

Inspecting the main-function using IDA (use F5 to see the decompiled code):

![](https://i.imgur.com/tLEB2Rk.png)

This `cek` seems to be all important. Let's see what that function does:

![](https://i.imgur.com/gm1ZjB7.png)

So it compares the argument to a value called `valid`. Let's see what that value is:

![](https://i.imgur.com/YlwgXUg.png)

Which is hexadecimal for 333333 (IDA can convert hex to decimal, just right click the value). This is the pin, which is the flag.