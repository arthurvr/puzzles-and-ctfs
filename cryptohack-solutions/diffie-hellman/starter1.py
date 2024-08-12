p = 991
g = 209

# "Find the inverse element d such that g * d mod 991 = 1"
d = pow(g, -1, p)
print(d)
