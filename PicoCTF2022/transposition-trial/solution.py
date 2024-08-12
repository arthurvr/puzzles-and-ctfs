ciphertext = "heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V9AAB1F8}7"

plaintext = ""
for i in range(0, len(ciphertext), 3):
    plaintext += ciphertext[i+2] + ciphertext[i] + ciphertext[i+1]

print(plaintext)
