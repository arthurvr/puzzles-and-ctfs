# MSB

> This image passes LSB statistical analysis, but we can't help but think there must be something to the visual artifacts present in this image...

Changing the LSB (*Least Significant Bit*) of a colour does not visually change the image (much): the effect is very small. But changing the MSB (*Most Significant Bit*) of an image does change the image visually. That's very visible in the given image indeed! In the image, we can even see the point where the image is normal again and the encoding on the MSB stops.

Let's try to extra the data in the MSB bits using [stegsolve](https://www.aldeid.com/wiki/Stegsolve). I installed stegsolve using these commands:

```
wget https://github.com/eugenekolo/sec-tools/raw/master/stego/stegsolve/stegsolve/stegsolve.jar
java -jar stegsolve.jar
```

Then I opened the file, and tried to extract data from the MSB bits of every color. Indeed, I found text:

![](https://i.imgur.com/SPDZzU3.png)

I saved this to `found_text.txt` and used vim to search for a `pico...` flag:

![](https://imgur.com/WzYbiF8.png)
