# Sum-O-Primes

> We have so much faith in RSA we give you not just the product of the primes, but their sum as well!

Again, you have to be aware of some of the maths behind RSA to solve this. If we know both the sum and the product of *p* and *q*, calculating the totient of n becomes easy:

```
totient of n = (p - 1) * (q - 1)
             = pq - p - q + 1
             = product - sum + 1
```

This totient is what we need to calculate the private exponent as `d = pow(e, -1, n - b + 1)`. Using that private exponent, calculate the plaintext as `pow(c, d, n)`. This is all done in `solution.py`:


```
┌──(arthur㉿kali)-[~/pico/sum-o-primes]
└─$ python solution.py
b'picoCTF{pl33z_n0_g1v3_c0ngru3nc3_0f_5qu4r35_92fe3557}'
```
