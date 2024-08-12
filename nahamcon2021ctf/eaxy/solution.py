flag = [' ']*38

for key in list(range(256)):
    eaxy_file = open('eaxy', 'rb')
    b = bytearray([c ^ key for c in eaxy_file.read()])

    if b'The XOR key you used' in b:
        for i in b.split(b'this is the ')[1:]:
            flag[int(i[0:2])] = chr(key)

    eaxy_file.close()

print(''.join(flag))