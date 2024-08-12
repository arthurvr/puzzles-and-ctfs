def sum_of_squares(lst):
	return sum(map(lambda x: x**2, lst))

def square_of_sum(lst):
	return sum(lst)**2

rng = range(101)
print(square_of_sum(rng) - sum_of_squares(rng))
