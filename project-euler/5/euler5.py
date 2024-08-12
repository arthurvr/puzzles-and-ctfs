def divisible(number, divisors):
	return all([number % divisor == 0 for divisor in divisors])

# These are really the only ones we have to check for as we increment by 2520
divisors = [11, 13, 16, 17, 19]

i = 2520
while (not divisible(i, divisors)):
	i += 2520
print(i)
