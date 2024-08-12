# Ambush Mission

I first tried all the usual when I'm given an image file: nothing from `binwalk`, nothing from `steghide`, nothing special in the exif-data, nothing from `zsteg`. 

There's one I don't always try but this image seems like a good candidate: having a look at the layers in the image with `stegoveritas`. One of the red ones is this one:

![](https://i.imgur.com/abCifC6.png)

Clearly not a "natural" part of the given image so interesting to us. The text (`==QTh9lMx8Fd08VZt9FdFNTb`) looked to me like a base64 encoding, but reversed (because of the two equal signs in front). Cyberchef can easily reverse the string and decode it: `m3Et_me_4t_12_aM`. This is the flag :)
