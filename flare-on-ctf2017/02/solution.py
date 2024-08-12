# From https://gist.github.com/Dliv3/d011325312292182a9674797761d2b41
# def _rol(val, bits, bit_size):
#     return (val << bits % bit_size) & (2 ** bit_size - 1) | \
#            ((val & (2 ** bit_size - 1)) >> (bit_size - (bits % bit_size)))

# __ROL4__ = lambda val, bits: _rol(val, bits, 32)

# print(hex(__ROL4__(0x80070000, 4) >> 1))
# The first key is this number (0x380004), but as an unsigned __uint16, so that's 0x4.

key = 0x4

encoded_flag = [0x0D, 0x26, 0x49, 0x45, 0x2A, 0x17, 0x78, 0x44, 0x2B, 0x6C, 0x5D, 0x5E, 0x45, 0x12, 0x2F, 0x17, 0x2B, 0x44, 0x6F, 0x6E, 0x56, 0x09, 0x5F, 0x45, 0x47, 0x73, 0x26, 0x0A, 0x0D, 0x13, 0x17, 0x48, 0x42, 0x01, 0x40, 0x4D, 0x0C, 0x02, 0x69, 0x00]
decoded_flag = []

for i in range(len(encoded_flag) - 1, -1, -1):
    decoded_flag.append(encoded_flag[i] ^ key)
    key = encoded_flag[i] ^ key

# Convert to string
decoded_flag = ''.join([chr(c) for c in decoded_flag])

# As we're evaluating the characters in the reverse order
decoded_flag = decoded_flag[::-1]

print(decoded_flag)

