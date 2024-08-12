# Tux!

> The flag is hidden inside the Penguin! Solve this challenge before solving my 100 point Scope challenge which uses similar techniques as this one.

I used binwalk to extract some embedded files: there's an embedded zip file, but it is password-protected.

I also called `file` on the `Tux.jpg` file, and there's a curious `comment` in there again. The comment is `ICAgICAgUGFzc3dvcmQ6IExpbnV4MTIZNDUK`, which is base64 for `Password: Linux12.45`. Makes sense!

The zip file opens with this password, and contains the flag `CTFlearn{Linux_Is_Awesome}`.

