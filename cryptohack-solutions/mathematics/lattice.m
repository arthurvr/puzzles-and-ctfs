# This challenge is about calculating the volume of the fundamental domain with given basis vectors.

v1 = [6; 2; -3];
v2 = [5; 1; 4];
v3 = [2; 7; 1];

# Result (flag): 255
abs(det([v1 v2 v3]))
