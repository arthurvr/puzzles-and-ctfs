# This challenge is an introduction to vector mathematics. This one is about
# calculating a dot product.

v = [2; 6; 3];
w = [1; 0; 0];
u = [7; 7; 2];

left = 3*(2*v - w);
right = 2*u;
dot(left, right)      # Answer (flag): 702
