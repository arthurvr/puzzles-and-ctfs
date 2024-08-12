# Application 1

Apparently, we're looking for a serial number that will pass this check:

![](https://i.imgur.com/iJr12f9.png)

This serial number could simply be hard-coded in the program. I could use a sophisticated reverse  engineering tool, like IDA, but I tried opening the program up in a simple hex editor first. Right before the *"Congrats, the password is ..."* message, there is indeed something that looks like a license key:

![](https://i.imgur.com/NlRqgh9.png)

Seems like it works:

![](https://i.imgur.com/ERm4k2p.png)
