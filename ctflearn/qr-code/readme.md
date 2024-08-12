# QR Code

> Do you remember something known as QR Code?

The QR code that's given contains the following string:

```
c3ludCB2ZiA6IGEwX29icWxfczBldHJnX2RlX3BicXI=
```

You don't need a phone to figure that out, there's free sites online.

I threw it into cyberchef and tried some stuff. The `=` sign at the end hints at base 64. But it's not readable yet, it looks like I need a second step. I had to try a bit of different stuff, but apparently, it's ROT13 for

```
flag is : n0_body_f0rget_qr_code
```
