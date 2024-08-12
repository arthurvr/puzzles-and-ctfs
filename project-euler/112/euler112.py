def digits(n):
	if n == 0:
		return []
	return digits(n // 10) + [n % 10]

def is_bouncy(n):
	digs = digits(n)
	isInc = False
	isDec = False
	for i in range(1, len(digs)):
		isInc = isInc or digs[i] > digs[i-1]
		isDec = isDec or digs[i] < digs[i-1]

		if isInc and isDec:
			return True
	return False

i = 1
count = 0
proportion = 0

while proportion < 0.99:
	i += 1
	if is_bouncy(i):
		count += 1
		proportion = count / float(i)

print(i)
