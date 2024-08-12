# Application 14

> It's Windows only for a reason.

It's often a good idea to check out what kind of executable we got with *Detect It Easy* first. In this case, we got a very old VB.NET program:

![](https://i.imgur.com/oJQMU4I.png)

I like using [ILSpy](https://github.com/icsharpcode/ILSpy) when dealing with .NET reverse engineering. The main program is in the `goes` class, some encryption/decryption utilities in the `Encrypt` class. The if-statements look impossible... we simply always end up in the case with the *sorry*-message. It looks like the password will simply be the decryption of ``"fm`{f}kpwrn"``.

![](https://i.imgur.com/Qal4BLv.png)

The decryption procedure looks like some very simple math:

![](https://i.imgur.com/m2XwcT2.png)

So I simply created a program that does the decryption of the ciphertext:

![](https://i.imgur.com/csS356f.png)

That's the password indeed!
