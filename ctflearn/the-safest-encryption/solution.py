# The two given files are exactly the same size... suspicious!
# So I tried to just XOR the two files into a new pdf file.

file1 = bytearray(open("given/CTFLearn.txt", "rb").read())
file2 = bytearray(open("given/CTFLearn.pdf", "rb").read())

result = bytearray(min(len(file1), len(file2)))

for i in range(len(result)):
    result[i] = file1[i] ^ file2[i]

open('result.pdf', 'wb').write(result)
