# Forensic 1

* The given file is a `tar` archive. Un-archive it to find a `.dd` file (a disk image).
* I used [`foremost`](https://www.kali.org/tools/foremost/) on this image (with some randomly chosen extensions of interest). Foremost is included in Kali Linux by default.

![](https://i.imgur.com/laBEOYL.png)

* Foremost generates a nice overview of the files it found in a txt file. The password-protected rar-archives are interesting...

![](https://i.imgur.com/KdV4Q9o.png)

* I listened to the audio file (the `wav`). It's a voicemail recording, where someone mentions to use a phone number as key.

* I started looking for phone numbers in the other documents. Found one in this `docx`:

![](https://i.imgur.com/64WSjCf.png)

*(You can install Libreoffice to open these on Kali Linux - or use the online Microsoft Office versions).*

* Indeed, this phone number (without the `-`-characters) worked as password to the `rar` file. The archive contained a new `docx`, with the challenge password :)

![](https://i.imgur.com/vZURnuG.png)

