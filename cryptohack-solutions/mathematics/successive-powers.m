# Challenge:
#
# "The following integers: 588, 665, 216, 113, 642, 4, 836, 114, 851, 492, 819,
#  237 are successive large powers of an integer x, modulo a three digit prime p.
#  Find p and x to obtain the flag. The flag is crypto{p,x}."
#
# This is the kind of challenge you'd probably just want to do using pen and paper...

t = [588; 665; 216; 113; 642; 4; 836; 114; 851; 492; 819; 237];

# We know that t[2] = t[1] * x mod p
#              t[3] = t[2] * x mod p
#              t[4] = t[3] * x mod p
#              ...

# So let's just iterate over the possible p values, and see if we get a
# consistent solution for x?

for p = [100:999]
  [G1, C1, ~] = gcd(t(1), p);
  [G2, C2, ~] = gcd(t(2), p);

  if G1==1
    if G2==1
      ModMultInvOfT1 = mod(C1,p);
      ModMultInvOfT2 = mod(C2,p);

      x1 = mod(t(2)*ModMultInvOfT1, p);
      x2 = mod(t(3)*ModMultInvOfT2, p);

      if x1 == x2
        p
        x = x1
      endif
    endif
  endif
end
