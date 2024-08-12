# Rangoon

As I did for lots of the reversing challenges, I started by opening this file in IDA. I found out some stuff about the flag immediately. 

The flag format is as expected:

![](https://i.imgur.com/8qiQAcI.png)

This check gives away the length of the flag: 28 characters.

![](https://i.imgur.com/IFyDRgk.png)

And these checks give away the location of some underscore characters:

![](https://i.imgur.com/Uc3lq80.png)

This list of words in memory also looked interesting, but I didn't quite figure out what it's used for:

![](https://i.imgur.com/N9nZoTi.png)

I was a little stuck in IDA so then I decided to run the program with GDB, and put a breakpoints on the way to the *"correct flag"* message. At one of the breakpoints, this flag was in one of the registers: 

![](https://i.imgur.com/2nObTOc.png)

Really strange, as this is not the correct flag (it's not even the correct length). However, I think it gives away the correct format of the flag. It seems like the flag (with the right length and underscores in the right place), should be in this format:

```
CTFlearn{xxxxxxxx_xxxx_xxxx}
```

Where the x-characters should be words from the list I found. Luckily, there's not that much words in there, and the lengths are quite distinctive. So there's only a very small number of possible flags. I tried two and already found the right one:  `CTFlearn{Princess_Maha_Devi}`.
