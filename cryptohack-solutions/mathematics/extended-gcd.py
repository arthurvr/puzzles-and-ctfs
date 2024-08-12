# Challenge:

# Using the two primes p = 26513, q = 32321, find the integers u,v such that
#   p*u + q*v = gcd(p,q)
# Enter whichever of u and v is the lower number as the flag.

# Solution:
# Because p and q are primes, gcd(p,q)=1. So we have to solve:
# 26513 * u + 32321 * v = 1

# This returns [gcd(a,b), u, v]
def extended_euclid_gcd(a, b):
    s = 0; old_s = 1
    t = 1; old_t = 0
    r = b; old_r = a

    while r != 0:
        L = old_r // r
        old_r, r = r, old_r - L * r
        old_s, s = s, old_s - L * s
        old_t, t = t, old_t - L * t
    return [old_r, old_s, old_t]

[gcd, u, v] = extended_euclid_gcd(26513, 32321)
assert gcd == 1
print(min(u, v))
