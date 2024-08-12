# Lemur XOR

> I've hidden two cool images by XOR with the same secret key so you can't see them!

> This challenge requires performing a visual XOR between the RGB bytes of the two images - not an XOR of all the data bytes of the files.

```py
from PIL import Image, ImageChops
im1 = Image.open('lemur.png')
im2 = Image.open('flag.png')

# im1 = lemur ^ key
# im2 = flag ^ key
# im3 = im1 ^ im2 = lemur ^ flag

# It's not perfect but let's just calculate abs(a-b) instead of (a-b)^2 (which would be the real XOR operation)

im3 = ImageChops.add(ImageChops.subtract(im2, im1), ImageChops.subtract(im1, im2))
im3.show()
```

The result:

![](https://i.stack.imgur.com/2L77k.png)
