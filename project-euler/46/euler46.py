primes = set()

def is_prime(n):
	return all(n % p for p in primes)

n = 33
while True:
	if is_prime(n):
		primes.add(n)
	else:
		if not any((n - 2*i*i) in primes for i in range(1, n)):
			break
	n += 2

print(n)
