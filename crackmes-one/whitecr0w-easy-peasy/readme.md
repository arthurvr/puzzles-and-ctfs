# whitecr0w's Easy Peasy

> Just created this program to learn more about Reverse Engineering. It should be pretty easy.

Found this challenge on **crackmes.one**: [link](https://crackmes.one/crackme/5d295dde33c5d410dc4d0d05)

## Solution

I opened the program in IDA and the username and password were pretty obvious in the *Strings* subview:

![](https://i.imgur.com/tokEVIP.png)
![](https://i.imgur.com/dIpbKrS.png)

Wasn't really necessary anymore, but I still went looking for the username/password comparison code and renamed some variables for clarity.
As IDA recognised the calls to `std::operator==` that wasn't very difficult either:

![](https://i.imgur.com/UkzUfEZ.png)