# HMX0101's DecryptMe #1

>  Analyze the algo, reverse the algo, decrypt the goodboy message. Patching is not allowed.

*[](https://crackmes.one/crackme/5ab77f6133c5d40ad448c8dd)*

## Solution

### 1. Reversing the algorithm

![](https://i.imgur.com/Z03srHC.png)

The challenge is immediately quite clear: find a key to enter that gets us a message that makes sense. (*"The goodboy message"*) I can only enter numbers in the input field, and the pop-up always shows something (albeit nonsense), so there is no process in place to check if the key is correct.

I used IDA again. I tried the strings subview  first, but didn't find much useful stuff. So then I went looking for calls to `MessageBox` instead and found the relevant code.

After entering a key, this happens first. It is the routine that converts a string with integer characters to an actual integer. Like I noticed before, look at how it skips anything < '0' or > '9'.

![](https://i.imgur.com/wSFejJm.png)

After this routine (sub_13E1C), there's this routine that looks a lot like a decryption process:

![](https://i.imgur.com/sbMUQNc.png)

Looks like the encryption happens character-per-character, so keys will be <= 255.

What I think is happening, for every character:
1. Subtract `0x2644`
2. XOR with `0x0DEAD`
3. Add `10`
4. Subtract the key
5. XOR the key
6. Bitwise-AND `0xFF`

That's an algorithm we can easily replicate in any scripting language :-)


### 2. Finding the ciphertext

By putting a breakpoint right before the decryption call and checking out AEX, I found this piece of memory. It's the ciphertext.

![](https://i.imgur.com/Jrg7hUf.png)

### 3. Cracking the key

Assuming the plaintext is in English, an attack that does a letter-frequency analysis would be feasable. However, I tried something simpler first. The script in `decrypt.py` decrypts using all possible keys, and only prints the plaintexts that are completely in the printable spectrum of ASCII characters. Looks like that's enough, as there's not that much options and you can easily see which plaintesxt makes sense:

![](https://i.imgur.com/G5W0rE5.png)
![](https://i.imgur.com/vrvYgpP.png)

