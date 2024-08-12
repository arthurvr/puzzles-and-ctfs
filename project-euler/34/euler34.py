from math import factorial

def digits(n):
	return [int(c) for c in str(n)]

def digits_factorial(n):
	return sum(map(factorial, digits(n)))

# The upper bound here is 9!*7 (see https://en.wikipedia.org/wiki/Factorion)
solution = sum(filter(lambda x: digits_factorial(x) == x, range(10, factorial(7)*9)))

print(solution)
