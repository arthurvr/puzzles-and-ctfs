# pranav's FindMySecret

[Link](https://crackmes.one/crackme/6005140733c5d42c3d016718)

## Given readme

The zip contains a readme file:

```
THis is FindMySecret by pranav.

This one will be a bit different from the other crackmes. There is no hardcoded password in this to find. 

My executable, when executed, will generate a secret number and store it. Then you will be asked to 'guess' it. You have 6 turns to find the number, or the executable will be killed and the number will be gone. 

As it's generating it's own secret number everytime, this one will not have a solution password. So, the solution is how you found the secret number, explained detailed. And maybe a screenshot is appreciated :)

I would suggest to upload the writeup and screenshot as a ZIP file. Good Luck!

(Hint: Don't quit the app after trying just once. You might just get something..)
```

## Solution

Seems like there's a range (maybe 1-10000?) the number must be found in:

![](https://i.imgur.com/rtqVgbX.png)

IDA did not immediately bring me to the right functions, but after some browsing (and using the strings subview) I found this code:

![](https://i.imgur.com/znmfwHU.png)

If the range is 0-10000  indeed, this code makes lots of sense: a random double (between 0 and 1) is probably generated and then multiplied by 10000. That would  explain the if-statement in this code block too. Let's start a debugger (I used x32dbg) and have a look at this address (`0x004063e8`). I changed the settings to display that memory location is a 64-bit double first of course:

![](https://i.imgur.com/LaL7IOj.png)

This makes sense: it's 0.84187 now, which will be multiplied by 10000. Let's try:

![](https://i.imgur.com/wCqrr10.png)

Yay!
