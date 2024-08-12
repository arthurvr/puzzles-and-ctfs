objects = [
    21, 12, 32, 32, 18, 35, 29, 26, 11, 34, 25, 38, 4, 7, 12,
    28, 38, 10, 11, 13, 28, 38, 32, 28, 21, 11, 38, 16, 23, 13,
    17, 38, 31, 16, 15, 2, 38, 15, 25, 27, 27, 38, 27, 23, 34, 33, 39
] 

letters = ["1234567890QWERTYUIOPASDFGHJKL{ZXCVBNM_-}"[i] for i in objects]

print("".join(letters))

# Result: SECCON{JWBH-58EL-QWRL-CLSW-UFRI-XUY3-YHKK-KFBV}