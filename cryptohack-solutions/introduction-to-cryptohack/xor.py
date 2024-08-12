from pwn import xor
given = b"label"
print("crypto{" + xor(given, 13).decode("utf-8") + "}")