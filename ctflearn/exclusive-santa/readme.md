# Exclusive Santa

> Hey! There are so many toys that I want, but I just don't have the money. I don't care which toy I get as long as it's one or the other, but not both!

*Notice how the challenge text hints at a XOR operation ;)*

1. The given file is a `rar` archive. Unarchiving it, I found two files `1.png` and `3.png`.

2. The images don't really look alike, so XORing these two doesn't seem like a good idea. So I first tried `binwalk` to see if there were more files in there.. And indeed there were! There's a file inside `3.png` that looks very much alike `1.png`. I called this `2.png`.

3. When I XOR this `1.png` with the new `2.png` I get the following:

![](https://i.imgur.com/fVmAQpj.png)

As I didn't find an online tool to easily XOR two PNG files, I used the PIL python module and the following script:

```py
from PIL import Image, ImageChops

def get_xor(image_1, image_2):
    i1 = ImageChops.invert(image_1)
    i2 = ImageChops.invert(image_2)

    return ImageChops.invert(ImageChops.add(ImageChops.subtract(i2, i1), ImageChops.subtract(i1, i2)))

image1 = Image.open("1.png")
image2 = Image.open("2.png")

result_image = get_xor(image1, image2)
result_image.save("result.png")
```

4. I guess the flag is technically readable already, but a small rotation with any image editing tool helps a lot:

![](https://i.imgur.com/2sSRpqp.png)
