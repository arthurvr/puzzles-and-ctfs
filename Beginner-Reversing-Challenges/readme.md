# Beginner-Reversing-Challenges: Notes

> Some notes and code while doing these awesome reverse engineering challenges by [MalwareTech](https://github.com/MalwareTech/Beginner-Reversing-Challenges)

There's an excellent [YouTube series](https://www.youtube.com/@MalwareTechBlog/videos) from Marcus too. I used IDA to do these challenges, just like him. I included the original challenges in zip files (pw: `MalwareTech`) just so I would never lose them.

## `strings1`

This program just prints an MD5 hash of the flag to the screen.

These challenges are all based on the fact that a naive reverse engineer will simply use a tool like `strings` (printing out all the strings in a program). This is made impossible here (I used the IDA-version of such a tool, *View > Open subview > strings*):

![](https://i.imgur.com/DOy5UGq.png)

However, actually inspecting the start function and looking at what it does, it's all rather obvious.

![](https://i.imgur.com/3tygbMW.png)

The flag is in there. It's `FLAG{CAN-I-MAKE-IT-ANYMORE-OBVIOUS}`. It is the parameter passed to the MD5 procedure. The hash ends up in the EAX register, and gets passed later to the `MessageBox`.

## `strings2`

Again, this program prints the hash of the flag to the screen.

IDA is really good, as it makes it a little too obvious again:

![](https://i.imgur.com/Z64y71E.png)

This is called string stacking: splitting the string to make it less readable. Tip: IDA changes hex values to characters by pressing the R key. We can even select all the strings and press R only once.

The flag is `FLAG{STACK-STRINGS-ARE-BEST-STRINGS}`.

## `strings3`

Again a program that prints a hash to the screen. This one is not that obvious. However, IDA makes it quite clear which function calls happen in `start`. We can look their definition up online.

![](https://i.imgur.com/SUgTx5z.png)

* The call to `FindResourceA` loads a resource segment with name `"rc.rc"`.
* The call to `LoadStringA` loads a string from that resource segment. The `UINT` parameter determines which string, so we have to figure out what it is set to. It's set to the result of a calculation using shifts (`shl`) - so a simple calculator can help us figuring out what that calculation will result to.

```
AEX = 1 << 8 = 256
EDX = 1 << 4 = 16
AEX + EDX = 272
```

Apparently IDA is not good at handling resources, so I used PE Explorer to find out which string we actually load. 

* Then the usual call to `MessageBoxA`
* And an `ExitProcess` call.

So, the flag is stored in the resources (which is a popular technique in malware):

![](https://i.imgur.com/FwqJMvy.png)

The flag is `FLAG{RESOURCES-ARE-POPULAR-FOR-MALWARE}`.

## `shellcode1`

The *F5* decompilation gives a pretty clear overview of what the code is doing. It is even more useful when we start to rename some variables. The `Str` is clearly encrypted as it looks like gibberish, and it looks like the code doing the decryption should be the shellcode. The shellcode is in the space allocated by the `VirtualAlloc` call, and it's put there using the `memcpy` call.
 
![](https://i.imgur.com/NBjO7g1.png)

So what shellcode are we actually copying there? What shellcode is at `unk_40468`? While inspecting the data, we can use the C key to convert it to code:

![](https://i.imgur.com/6tya7aA.png)

Looks like a ROL operation: [StackOverflow to the rescue!](https://stackoverflow.com/questions/3057726/how-to-get-bit-rotation-function-to-accept-any-bit-size) We can then use this Python program to decrypt the `Str` ourselves.

```python
def ROR(x, n, bits=8):
    mask = (2**n) - 1
    mask_bits = x & mask
    return (x >> n) | (mask_bits << (bits - n))

def ROL(x, n, bits=8):
    return ROR(x, bits - n, bits)

encrypted_flag = bytearray([
	0x32, 0x62, 0x0A, 0x3A, 0xDB, 0x9A, 0x42, 0x2A, 0x62, 0x62, 0x1A, 0x7A, 0x22, 0x2A, 0x69, 0x4A, 0x9A, 0x72, 0xA2, 0x69, 0x52, 0xAA, 0x9A, 0xA2, 0x69, 0x32, 0x7A, 0x92, 0x69, 0x2A, 0xC2, 0x82, 0x62, 0x7A, 0x4A, 0xA2, 0x9A, 0xEB
])

flag = bytearray([0] * len(encrypted_flag))

for i in range(len(encrypted_flag)):
	flag[i] = ROL(encrypted_flag[i], 5)

print("The flag: ")
print(flag)

```

The result gives us the flag:

![](https://i.imgur.com/cpvGvYo.png)

Tip: exporting the contents of `Str` to Python was easy using *Edit > Export Data*:

![](https://i.imgur.com/bZpyz6X.png)

## `shellcode2`

At first glance, this seems like a combination of previous techniques: there's some string stacking, and again a call to heap (= shellcode). There's also calls to two functions I haven't seen before in these challenges. They seem to involve dynamic function resolution:

* `GetProcAddress`: Retrieves the address of an exported function from a DLL.
* `LoadLibrary`: Loads a module (taking a name).

The MD5 function takes the EDX register: the unencrypted flag should be there. So it should be in `var_28`. However, again, those values seem encrypted in the `start` routine. Somewhere it will be decrypting the flag!

The `var_4` is the address of some allocated memory. Judging by the code, it should look like this:

```
0x00    LoadLibrary
0x04    GetProcAddress
0x08    Flag (encrypted)
```

Using *Right click > Use standard symbolic constant* we can make the parameters that are being passed more clear: (We have to know or look them up ourselves though!)

![](https://i.imgur.com/uL72pnq.png)

The `var_C0` seems to be the executable part of the memory area. Looking at this, it is indeed shellcode. It is being called with a parameter, namely our other allocated memory. But this time the shellcode is more complicated: it's all stack strings. Let's use C to convert to chars (and unclick *Apply only if possible*):

![](https://i.imgur.com/gZjUQFe.png)

It contains first some strings:

```
msvcrt.dll
win32.dll
fopen
fread
fseek
fclose
GetModuleFilename
rb
```

... followed by the shellcode (= `exec_mem_area`). The first thing the shellcode does is getting the addresses of these functions and loading the libraries. Once we interpret the the file names, the reverse code becomes quite clear:

![](https://i.imgur.com/GtlgTQs.png)

Now, let's recreate this procedure in Python so we can safely execute it ourself.

```
# We already know what the file name is, so no need to recreate that call!
file_path = "C:\\Users\\arthu\\Documents\\Beginner-Reversing-Challenges\\shellcode2\\shellcode2.exe"

file = open(file_path, "rb")

# The fseek decides where in the file we're gonna read from (it sets the offset):
# We could check out where that is using HxD. -- Turns out it's where the DOS header string is.
file.seek(0x4E)


# Then the fread call: 1 count of 26 bytes
# So this simply reads the hader! "This program cannot be run in DOS mode"
data = file.read(0x26)
print(data)
```

![](https://i.imgur.com/APg8UIr.png)

After that, the encryption itself is XOR based: it XORs the DOS-header string with the encrypted flag. Similar to last time, we can use the export function again to get a Python byte array.

```
encrypted_flag = bytearray([
	0x12,
	0x24,
	0x28,
	0x34,
	0x5B,
	0x23,
	0x26,
	0x20,
	0x35,
	
	# ... 
])

dos_string = b"This program cannot be run in DOS mode"

for i in range(len(encrypted_flag)):
	encrypted_flag[i] = encrypted_flag[i] ^ dos_string[i]

print(encrypted_flag)
```

Yay!

![](https://i.imgur.com/KScqd6u.png)

## `ransomware1`

This is a basic ransomware setup: we need to recover encrypted files. The encryption procedure is given as an exe file. The encryption procedure (after renaming some variables) is this:

![](https://i.imgur.com/aTtg6Qo.png)

Conclusion: it's a simple XOR cipher (encrypting one byte at a time), with a 32 bytes long key, which is passed as a paramter.

The key, however, is not in the program... Luckily, this is vulnerable to a known plaintext attack! The windows sample pictures were encrypted too, and those originals are easily found online.

```python
ciphertext = open("C:\\Users\\arthu\\Documents\\Beginner-Reversing-Challenges\\ransomware1\\EncryptedFiles\\Pictures\\Sample Pictures\\Koala.jpg_encrypted", "rb")
ciphertext = ciphertext.read(512)
ciphertext = bytearray(ciphertext)

plaintext = open("C:\\Users\\arthu\\Documents\\Beginner-Reversing-Challenges\\ransomware1\\EncryptedFiles\\Pictures\\Sample Pictures\\Koala_original.jpg", "rb")
plaintext = plaintext.read(512)
plaintext = bytearray(plaintext)

key = plaintext
for i in range(len(plaintext)):
	key[i] = ciphertext[i] ^ plaintext[i]

# Key:
enc_flag = open("C:\\Users\\arthu\\Documents\\Beginner-Reversing-Challenges\\ransomware1\\EncryptedFiles\\Documents\\flag.txt_encrypted", "rb")
enc_flag = enc_flag.read(512)
enc_flag = bytearray(enc_flag)

for i in range(len(enc_flag)):
	print(chr(key[i] ^ enc_flag[i]), end='')
```

There we go:

![](https://i.imgur.com/s1qUzOK.png)
