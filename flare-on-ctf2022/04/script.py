v5 = [0]*35

v5[0] = 0x50
v5[1] = 0x5e
v5[2] = 0x5e
v5[3] = 0xA3
v5[4] = 0x4F
v5[5] = 0x5B
v5[6] = 0x51
v5[7] = 0x5E
v5[8] = 0x5E
v5[9] = 0x97
v5[10] = 0xA3
v5[11] = 0x80
v5[12] = 0x90
v5[13] = 0xA3
v5[14] = 0x80
v5[15] = 0x90
v5[16] = 0xA3
v5[17] = 0x80
v5[18] = 0x90
v5[19] = 0xA3
v5[20] = 0x80
v5[21] = 0x90
v5[22] = 0xA3
v5[23] = 0x80
v5[24] = 0x90
v5[25] = 0xA3
v5[26] = 0x80
v5[27] = 0x90
v5[28] = 0xA3
v5[29] = 0x80
v5[30] = 0x90
v5[31] = 0xA2
v5[32] = 0xA3
v5[33] = 0x6B
v5[34] = 0x7F

result = ""

# "Near return": https://www.felixcloutier.com/x86/ret
retn_instruction = 0xC3

for item in v5:
    result += chr(retn_instruction - item)

print(result)
