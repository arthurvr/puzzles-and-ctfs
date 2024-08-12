def sides(perimeter):
	possibilities = []
	for a in range(1, (perimeter//4) + 1):
		for b in range(1, (perimeter - a)//2):
			c = perimeter - a - b
			if a**2 + b**2 == c**2:
				possibilities.append((a, b, c))
	return possibilities

results = []
for p in range(1, 1001):
	results.append(sides(p))
print(results.index(max(results, key=len)) + 1)
