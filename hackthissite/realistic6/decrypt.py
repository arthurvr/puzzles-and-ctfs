ciphertext = open("ciphertext.txt").read()

numbers = list(map(lambda x: int(x.strip()), ciphertext.strip(".").split(".")))
numbers = list(zip(*[numbers[i::3] for i in range(3)]))
numbers = list(map(lambda t: t[0]+t[1]+t[2], numbers))

i = 1
while True:
	i += 1
	mod_numbers = list(map(lambda x: x - i, numbers))
	plaintext = "".join([chr(c) for c in mod_numbers])
	if "Samuel" in plaintext:
		print(plaintext)
		break
