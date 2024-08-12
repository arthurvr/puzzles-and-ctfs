def canoodle(panjandrum, arylo, s, bibble):
    kerfuffle = bytearray()
    quean = 0
    for cattywampus in range(0, len(panjandrum), 4):
        kerfuffle.append(int(panjandrum[cattywampus + arylo:cattywampus + arylo + 2], 0x10) ^ bibble[quean % len(bibble)])
        quean += 1
        if quean == s:
            break
    return kerfuffle

flareon = b"FLARE-ON"
invflareone = flareon[::-1]
wabbit = canoodle(F_T, 2, 285729, bytearray(invflareone))

with open("result.png", "wb") as mp3file:
    mp3file.write(wabbit)