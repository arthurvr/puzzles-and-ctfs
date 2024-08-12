from math import log

f = open('base_exp.txt')
lines = f.readlines()
pairs = [list(map(lambda x: int(x.strip()), line.split(','))) for line in lines]

# The line representing the largest number will also have the largest logarithm!
# log(base ^ exp) = exp * log(base)
logarithms = [exp * log(base) for base, exp in pairs]

print(logarithms.index(max(logarithms)) + 1)
