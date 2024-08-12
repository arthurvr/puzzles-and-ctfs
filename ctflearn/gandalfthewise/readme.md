# GandalfTheWise

> Extract the flag from the Gandalf.jpg file. You may need to write a quick script to solve this.

Inspired by the challenges I previously solved, I first called `file` on the file...


```
$ file gandalf.jpg
gandalf.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, comment: "Q1RGbGVhcm57eG9yX2lzX3lvdXJfZnJpZW5kfQo=", comment: "xD6kfO2UrE5SnLQ6WgESK4kvD/Y/rDJPXNU45k/p", comment: "h2riEIj13iAp29VUPmB+TadtZppdw3AuO7JRiDyU", baseline, precision 8, 225x225, components 3
```

The first comment is base64 for `CTFlearn{xor_is_your_friend}`. I tried this flag, but it's incorrect. However, it's a good hint: I'll probably have to use XOR. Let's maybe XOR the (base64 decoding?) of the other two comments?

That worked! See the Python script in this folder :)
