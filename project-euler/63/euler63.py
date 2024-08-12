count = 0

for i in range(1, 10):
	power = 1
	while power == len(str(i ** power)):
		count += 1
		power += 1

print(count)
