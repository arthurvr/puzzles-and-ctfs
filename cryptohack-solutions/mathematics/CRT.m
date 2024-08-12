# Challenge on the Chinese Remainder Theorem

# " Given:
#    x ≡ 2 mod 5
#    x ≡ 3 mod 11
#    x ≡ 5 mod 17
#
#    Find an x such that x ≡ a mod 935."

a1 = 2;
n1 = 5;
m1 = 11*17;

# Calculates the inverse of m1 mod n1
[G1, C1, ~] = gcd(m1, n1);
if G1==1
  inv_m1 = mod(C1, n1);
endif

a2 = 3;
n2 = 11;
m2 = 5*17;
[G2, C2, ~] = gcd(m2, n2);
if G2==1
  inv_m2 = mod(C2, n2);
endif

a3 = 5;
n3 = 17;
m3 = 11*5;
[G3, C3, ~] = gcd(m3, n3);
if G3==1
  inv_m3 = mod(C3, n3);
endif

M = n1*n2*n3;

# Result (flag): 872
solution = mod(a1*m1*inv_m1 + a2*m2*inv_m2 + a3*m3*inv_m3, M)


