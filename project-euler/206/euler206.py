from math import sqrt

def digits(n):
	return [int(c) for c in str(n)]

def check_solution(x):
	digs = digits(x)
	return digs[0] == 1 and digs[2] == 2 and digs[4] == 3 and digs[6] == 4 and digs[8] == 5 and digs[10] == 6 and digs[12] == 7 and digs[14] == 8 and digs[16] == 9 and digs[18] == 0

# All numbers replaced by 0, and by 9
minnum = round(sqrt(1020304050607080900))
maxnum = 1389026630 # round(sqrt(1929394959697989990))

# Last digit is 0 so we should only check multiples of 10
for i in range(maxnum, minnum, -10):
	if check_solution(i * i):
		print(i)
		break
