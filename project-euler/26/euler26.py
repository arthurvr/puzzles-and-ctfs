def get_cycle_length(denominator):
    digits = []
    remainders = []

    cur = 10

    while True:
        digit, cur = divmod(cur, denominator)
        if cur in remainders:
            break

        digits.append(digit)
        remainders.append(cur)

        cur *= 10
        if cur == 0:
            return 0
        while cur < denominator:
            cur *= 10
            digits.append(0)

    while remainders[0] != cur:
        remainders.pop(0)

    return len(remainders)


max_i, max_length = -1, -1
for i in range(1, 1000):
	l = get_cycle_length(i)
	if l > max_length:
		max_i = i
		max_length = l

print(max_i)
