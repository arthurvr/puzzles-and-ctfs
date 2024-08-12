factorials = [1,1,2,6,24,120,720,5040,40320,362880]

def factorialDigitSum(n):
	if n < 10:
		return factorials[n]
	return factorials[n % 10] + factorialDigitSum(n // 10)

def sequence_length(n):
	seq = [n]
	while True:
		nextstep = factorialDigitSum(seq[-1])
		if nextstep in seq:
			return len(seq)
		else:
			seq += [nextstep]

result = 0
for i in range(1000000):
	if sequence_length(i) == 60:
		result += 1

print(result)
