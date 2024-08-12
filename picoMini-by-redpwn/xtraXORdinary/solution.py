# Known plaintext attack using the string "picoCTF{" to find the key :) 

# Small optimisations I did:
#  * The nested loops on lines 35 until 39 is useless.
#  * XORing with the same string twice is useless, so I removed some of the `random_strs`

from pwn import xor
from random import randint

ctxt = bytes.fromhex("57657535570c1e1c612b3468106a18492140662d2f5967442a2960684d28017931617b1f3637")

given_strs = [
    b'my encryption method',
    b'is absolutely impenetrable',
    b'and you will never',
    b'ever',
    b'break it'
]

flag = b""
while not flag.startswith(b"picoCTF{"):
    for given_str in given_strs:
        for m in range(randint(0, 2)):
            ctxt = xor(ctxt, given_str)

    known_plaintext = b"picoCTF{"
    key = xor(ctxt[:len(known_plaintext)], known_plaintext)
    # print("key: " + key.decode())
    # Some strings are not decodable, which results in an error. However, I got lucky quite fast as there's not much random ints between 0 and 2 :))

    key = b'Africa!'
    flag = xor(ctxt, key)

ptxt = flag.decode()
print(ptxt)