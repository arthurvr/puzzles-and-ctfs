counter = 0

file = open('triangles.txt', 'r')

for line in file.readlines():
	[x0, y0, x1, y1, x2, y2] = list(map(int, line.strip().split(',')))

	# Read: Barycentric coordinate system
	area = 0.5 *(-y1 * x2 + y0 * (-x1 + x2) + x0 * (y1 - y2) + x1 * y2);
	s = 1 / (2*area) * (y0 * x2 - x0 * y2);
	t = 1 / (2*area) * (x0 * y1 - y0 * x1);

	if s > 0 and t > 0 and (1-s-t) > 0:
		counter += 1

print(counter)
