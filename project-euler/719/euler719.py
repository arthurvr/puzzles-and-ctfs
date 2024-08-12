def is_sqrt_of_S_number(sqrt_value, n_result=None):
	if n_result is None:
		n = sqrt_value*sqrt_value
	else:
		n = n_result

	if n < sqrt_value:
		return False
	if n == sqrt_value:
		return True

	size = 10
	while size < n:
		quotient = n // size
		remainder = n % size

		if remainder >= sqrt_value:
			return False
		if is_sqrt_of_S_number(sqrt_value - remainder, quotient):
			return True
		size *= 10

	return False

# Looking at the S numbers for the simpler 10^4 example, I spotted that all S numbers seem to be either a multiple of 9,
# or equal to 1 modulo 9. Hence, I decided to only check those numbers...
# Also, note I'm using sqrt(10^12) = 10^6 here immediately...
range_to_check = list(range(9, 10**6 + 1, 9))
range_to_check += [i + 1 for i in range_to_check]

print(sum([sqrt_n * sqrt_n for sqrt_n in range_to_check if is_sqrt_of_S_number(sqrt_n)]))
