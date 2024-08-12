# "For the finite field with p = 28151 find the smallest element g which is a primitive element of Fp."
p = 28151

# The order of g modulo p is the smallest positive integer k with g^k = 1 mod p
def order(g, p):
    for i in range(2, p):
        if pow(g, i, p) == 1:
            return i
    return p

assert order(7, 288) == 12
assert order(30, 101) == 50

# Solution: We can check if the order of each element >= 2 is equal to p - 1. That's only the case when the number is a generator.
for g in range(2,p):
    if order(g, p) == p - 1:
        print(g)
        break
