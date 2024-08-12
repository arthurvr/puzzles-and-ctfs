import string
import random

def try_creating_serial():
    valid_chars = '-' + string.ascii_lowercase + string.ascii_uppercase + string.digits
    valid_chars = [ord(x) for x in valid_chars]

    ## Rock
    serial = [random.choice(valid_chars) for i in range(19)]

    ## Paper
    candidates = list(filter(lambda x: (x^serial[10]) <= 9, valid_chars))
    if len(candidates) == 0: return try_creating_serial()
    serial[8] = random.choice(candidates)

    candidates = list(filter(lambda x: (x^serial[13]) <= 9, valid_chars))
    if len(candidates) == 0: return try_creating_serial()
    serial[5] = random.choice(candidates)

    v2 = (serial[8] ^ serial[10]) + 48
    v3 = (serial[5] ^ serial[13]) + 48

    serial[3] = v2
    serial[15] = v2
    serial[0] = v3
    serial[18] = v3

    ## Scissors
    candidates = list(filter(lambda x: (x+serial[2]) > 170, valid_chars))
    if len(candidates) == 0: return try_creating_serial()
    serial[1] = random.choice(candidates)

    candidates = list(filter(lambda x: (x+serial[17]) > 170 and serial[1] + serial[2] != x+serial[17], valid_chars))
    if len(candidates) == 0: return try_creating_serial()
    serial[16] = random.choice(candidates)
    
    ## Cracker
    serial[4] = 45
    serial[9] = 45
    serial[14] = 45

    ## Convert to string
    return ''.join([chr(x) for x in serial])


print(try_creating_serial())
