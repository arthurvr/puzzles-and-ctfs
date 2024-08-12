# r0B's SanSuu

> You know the drill, get the good boy message.
> no patching, just a valid serial number and/or keygen.

*[Link](https://crackmes.one/crackme/606b1faf33c5d418e8c4009e)*

## Solution

Looks like we got an exe that prompts for a serial key, and tells us whether it's valid or not.

![](https://i.imgur.com/4Il8KYi.png)

I opened the given file up in IDA and found the relevant code quickly using the *Strings* subview.

![](https://i.imgur.com/G7vVg3e.png)

There's two small (intentional?) misdirections in this function:

* There seems to be some memory allocated for a `:D` string, but I don't think it's used anywhere.
* Instead of using some win-API functions directly, their address is passed as parameter. Once the parameters were renamed (according to how the function is called) everything became a lot more readable.

I renamed some other variables names too after checking some documentation for the API functions. Seems like only a first check happens here: the length of the given string should be between 4 and 12 and should be an odd number.
If this passes, another second function is called.

![](https://i.imgur.com/CV5yXMx.png)

This second function does a calculation, which should apparently result in `0` for the success message to be printed.

It's a recursive function, but following along with an example input using pen and paper makes the operations quite clear. Looks like the characters at even positions decide what will happen: adding or subtracting the characters add odd positions.

![](https://i.imgur.com/otYsBUp.png)

This is a seven-character serial which results in `0`, and indeed gets us the success message:

![](https://i.imgur.com/g0tyu29.png)

The calculation that happens is `'1' - ('0' - ('0' - ('1')))`... all subtractions because the even numbers also have an even ASCII code :)

Once you understand the recursive process behind the calculation, writing a keygen should be trivial. A keygen could even keep it simple and always choose even characters for all even positions, making the other choices easy.
