from pwn import xor

given = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")

# We know the beginning of the plaintext! Let's see what we can figure out
# known_plaintext = b"crypto{"
# key = xor(given, known_plaintext)
# print(key)

# It seems to be equal to b"myXORkey"
key = b"myXORkey"
plaintext = b""
for i in range(len(given)):
    plaintext += xor(given[i], key[i % len(key)])
print(plaintext)

