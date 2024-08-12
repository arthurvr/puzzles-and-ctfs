# Peach's crackme

> No patching. Make a keygen.

*[Link](https://crackmes.one/crackme/60461cf833c5d42c3d016d66)*


## Solution

I couldn't find a good entry point using the strings subview, so this time I went looking for all `MessageBoxW` calls. Looks like I found the all-important if-statement here that decides if I get the good-boy message.

![](https://i.imgur.com/0VzbeqF.png)

I assumed the first GetWindowTextA is for getting the name, and the second GetWindowTextA is for getting the serial.

That means the serial gets converted to an integer, and must be equal to the result of  this sub_401A94(name). Let's have a look at that function

![](https://i.imgur.com/gecbzAP.png)

Looks like this calculates v3 = 1 + (the sum of the characters of `name` except the first one). Then it calculates `(431136 * v3 - 3000) / 2 - *name`. Using a debugger I found `*name = 0xFFFFFFFFFFDC0790`, and this didn't seem to change. The result of this calculation is cast to an unsigned int. We have to be careful to cast to the same datatype, but replicating this calculating in a keygen can't be really difficult, especially if we use C too... I did so in 

![](https://i.imgur.com/ue4E7OQ.png)
![](https://i.imgur.com/u57S5IY.png)

I hardcoded the name `arthur` in `keygen.c` for now, but this could easily be a command line argument.