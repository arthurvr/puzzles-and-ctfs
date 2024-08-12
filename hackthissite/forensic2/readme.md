# Forensic 2

A JPEG file is given. One of the most complete tools to check out JPEG metadata I know is [JPEGsnoop](https://github.com/ImpulseAdventure/JPEGsnoop). Indeed, the compression signature looks like the file is photoshopped:

![](https://i.imgur.com/5BD0ZW3.png)

This is evidence of photoshop being used, but it's not a password yet... Then I was curious to see an [error level analysis](https://en.wikipedia.org/wiki/Error_level_analysis). I looked for an online tool that could do this and found `fotoforensics.com`:

![](https://i.imgur.com/XlIhRGn.png)

Ahh! This `ELA4LIFE!!` is the password.