from Crypto.Util.number import long_to_bytes

# Given:
e = 1
c = 9327565722767258308650643213344542404592011161659991421
n = 245841236512478852752909734912575581815967630033049838269083

# The d exponent will also be 1 because it's usually equal to pow(e, -1, totient(n)).

d = 1
plaintext = pow(c, d, n)
print(long_to_bytes(plaintext))
