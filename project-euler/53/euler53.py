from math import factorial

def choose(n, r):
	return factorial(n) / (factorial(r) * factorial (n-r))

count = 0
for n in range(1, 101):
	for r in range(1, n+1):
		if choose(n, r) > 1000000:
			count += 1

print(count)
