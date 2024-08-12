# Let me just cherry-pick the relevant information from the given text file instead of reading it:
key_uppercase = "VOUHMJLTESZCDKWIXNQYFAPGBR"
ciphertext = "ieuwUYJ{5FO5717F710K_3A0CF710K_357OJ9JJ}"

# Decryption process
key_lowercase = key_uppercase.lower()
plaintext = ""
for c in ciphertext:
    if c.isupper():
        plaintext += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[ key_uppercase.index(c) ]
    elif c.islower():
        plaintext += "abcdefghijklmnopqrstuvwxyz"[ key_lowercase.index(c) ]
    else:
        plaintext += c

print(plaintext)

