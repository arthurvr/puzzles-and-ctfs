# Bobby Toe's iPad

> Here is a pic of my friend Bobby Toe. while he's happy to give you his iPad, he's not as willing to give you the flag. can you get it from him? here is an image of Bobby Toe.

* Nothing special in `file` or `binwalk`.
* I also called `strings` on the file, and there's one noticable line in there:

```
congrats you found me! you win an iPad!
```

* Opening the file in a hex editor, there's something funny about the location of this string! If you delete the strange iPad-announcement completely, you make the JFIF signature bytes: `FF D8 FF E0 00 10 4A 46 49 46 00 01`. The iPad-string was just in the middle of this? 

* I just treated the edited file like any other now. Binwalk found a second file inside now:

![](https://i.imgur.com/kWREFC5.jpg)

* I also tried `zsteg`. One of the colour layers contained this:

![](https://i.imgur.com/9M4m87F.png)

* I think I'll have to combine these two strings in some way to find the flag? 
* Apparently, it's a [one-time pad](https://rumkin.com/tools/cipher/one-time-pad/)! I got `you_thinkyougotskillshuh` as a result, which is the correct flag!
