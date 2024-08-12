# Brute Force is Fun!

> You'll need Brute Force to solve this. Knowing Python should help too. Oh! And Base64 encryption of course! Find the flag!

> Hash: e82a4b4a0386d5232d52337f36d2ab73

It became clear immedatiately when using `strings` that the image file contained more than just an image. I used [foremost](https://www.kali.org/tools/foremost/) this time to extract those files. It contained a password-protected zip file.

I openend the zip file giving an empty password. The only files I could read contained this:

![](https://imgur.com/Xy8i0VE.png)

Fair enough, let's brute force now. See my script in `script.py`: it takes only a fraction of a second and got me the correct password for the `flag.zip`. 

The flag.txt file inside appears to contain base64:

![](https://imgur.com/URkESRA.png)
