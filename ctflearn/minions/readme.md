# Minions

> Hey! Minions have stolen my flag, encoded it few times in one cipher, and then hidden it somewhere there.

> Can you help me? TIP: Decode the flag until you got a sentence.

These are similar to the challenges before, but they're all nested. First find an embedded file using binwalk, then call `strings` on it to find a new `mega`-download link, then binwalk again to find the last image. Luckily the file names always make it pretty obvious where to go looking for the next file/step.

In the final file, using strings you'll find a base 64 encoded string, of a base 64 encoded string, of a base64 encoded string, ... of `CTF{M1NI0NS_ARE_C00L}`
