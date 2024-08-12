# Greedy_Fly's CrackMe v2.0

*[Link](https://crackmes.one/crackme/5ab77f6033c5d40ad448c88c)*

The program looks like a typical crackme: verifying the correctness of a serial code. I have a suspicion the correct serial will be the solution to the given chess problem (White to move, checkmate  black), but I first wanted to try actually reversing the code using IDA.

## Figuring out the serial length

The first part of the code seems to be about checking the length of the serial. The length is received by the system call, and then passed as a parameter to a separate routine. The result of this execution is compared to 148224.

![](https://i.imgur.com/b4WJWV9.png)

Having a look at what this function actually does, I think it calculates `(16 * (l+1) + 64) * 386`, where the multiplication by 16 happens using a shear instruction.

![](https://i.imgur.com/HKenSa7.png)

So which length actually makes this result in 148224?

![](https://i.imgur.com/zFLzsUO.png)

## Hashing code

The code after this looked like (quite a complicated) calculation, where these constants here are important:

![](https://i.imgur.com/BmsJtd8.png)

I looked for these constants using GitHub search, and apparently they're used in MD5. This makes sense, as earlier code looked like we were comparing to some kind of hash. Sure, MD5 is not considered secure anymore, but reversing a given hash is still a bit above my pay grade ;)

## Solving the chess Problem

Let's just see if solving the chess position helps me any further. I'm not a good chess player, but there are good calculators online:

![](https://i.imgur.com/8cFSGS7.png)

The complete solution is `a4bxa4b5a3Nb4Ka1Nb3`. Typically a `#` would be added at the end (representing the checkmate), but apparently I have to leave it out here:

![](https://i.imgur.com/g9srGV9.png)