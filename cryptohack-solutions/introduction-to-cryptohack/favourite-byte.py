from pwn import xor

given = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

# Just try all bytes and see if the plaintext contains b"crypto" 
for i in range(255):
    plaintext = xor(given, i)
    if b"crypto" in plaintext:
        print(plaintext)
