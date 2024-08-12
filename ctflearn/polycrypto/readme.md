# Polycrypto

> Polynomials are a very useful branch of mathematics. They can also hide secrets. Can you find what this one is hiding? 

Following polynomial is given:

```
f = x^206 + x^205 + x^202 + x^201 + x^198 + x^197 + x^195 + x^194 + x^190 + x^189 + x^184 + x^182 + x^181 + x^178 + x^177 + x^176 + x^174 + x^173 + x^172 + x^171 + x^169 + x^168 + x^166 + x^165 + x^164 + x^157 + x^156 + x^150 + x^149 + x^147 + x^146 + x^142 + x^141 + x^140 + x^139 + x^136 + x^134 + x^133 + x^131 + x^130 + x^129 + x^126 + x^125 + x^123 + x^122 + x^121 + x^120 + x^118 + x^117 + x^115 + x^114 + x^112 + x^109 + x^108 + x^104 + x^102 + x^101 + x^96 + x^94 + x^93 + x^91 + x^90 + x^86 + x^85 + x^84 + x^81 + x^80 + x^78 + x^76 + x^75 + x^74 + x^73 + x^72 + x^69 + x^68 + x^66 + x^62 + x^61 + x^60 + x^57 + x^53 + x^52 + x^49 + x^48 + x^46 + x^44 + x^43 + x^42 + x^41 + x^40 + x^38 + x^37 + x^35 + x^33 + x^32 + x^29 + x^28 + x^21 + x^20 + x^14 + x^13 + x^11 + x^10 + x^6 + x^5 + x^4 + x^3 + x^2 + 1
```

This can be converted a binary number (0 or 1 being the coefficient before x^i):

```
110011001101100011000010110011101111011011100000011000001101100011110010110111001101111011011010011000101100001011011000111001101011111001101000111001000110011010111110110101100110000001100000110110001111101
```

Or this number in hexadecimal:

```
666C61677B70306C796E6F6D31616C735F3472335F6B30306C7D
```

And using ASCII we get the following: 

```
flag{p0lynom1als_4r3_k00l}
```
