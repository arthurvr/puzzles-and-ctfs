# This challenge is about calculating the size of a given vector.

vec = [4; 6; 2; 5];

# Size = square root of inner product with itself
sqrt(dot(vec, vec))        # Result (flag): 9

# Easier would be norm(vec, 2)
