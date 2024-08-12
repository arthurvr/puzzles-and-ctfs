# Day 8: Have a Holly, Jolly Byte!

These are some exercises using [FTK Imager](https://www.exterro.com/ftk-imager) on a (virtual) USB drive connected to the VM.

* **What is the malware C2 server?** I first thought I was gonna have to reverse one of the malware files... but actually this wasmentioned in a chat (in the deleted directory). `mcgreedysecretc2.thm`

![](https://i.imgur.com/ko2A55O.png)

* **What is the file inside the deleted zip archive?** The zip is password-protected... but we don't need the password to see which files are inside. `JuicyTomaTOY.exe`

![](https://i.imgur.com/Ykw6zhe.png)

* **What flag is hidden in one of the deleted PNG files?** This is in the metadata, not the image itself! (search using Ctrl+F helps a lot...). `THM{byt3-L3vel_@n4Lys15}`

![](https://i.imgur.com/DJ6p5u6.png)

* **What is the SHA1 hash of the physical drive and forensic image?** `39f2dea6ffb43bf80d80f19d122076b3682773c2`

![](https://i.imgur.com/iZqTwg3.png)
