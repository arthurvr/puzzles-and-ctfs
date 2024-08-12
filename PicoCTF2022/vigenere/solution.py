message = "rgnoDVD{O0NU_WQ3_G1G3O3T3_A1AH3S_2951c89f}"
key = "CYLAB"

alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet_lower = "abcdefghijklmnopqrstuvwxyz"

def ceasar(input_char, n):
    if input_char.isupper():
        ind = (alphabet_upper.index(input_char) + n) % 26
        return alphabet_upper[ind]
    if input_char.islower():
        ind = (alphabet_lower.index(input_char) + n) % 26
        return alphabet_lower[ind]


plaintext = ""
key_index = 0
for i in range(len(message)):
    message_char = message[i]
    if message_char.isalpha():
        key_char = key[key_index % len(key)]
        offset = alphabet_upper.index(key_char)
        plaintext += ceasar(message_char, - offset)
        key_index += 1
    else:
        plaintext += message_char

print(plaintext)

