from gmpy2 import fac
from math import gcd
from Crypto.Util.number import *
from sympy import true

# Extracted from the given files:
n = 0x5837ab2dd26ff8ab827a4885c72229e2e908af1de303c35e1190659fb120acd3b256cd71d91cc25a96ed4261259c8928720217b1fb8fcc1002375f779ff64fc4f181715d882f304678bed6f376cb0497cb599d88dc4bb4563e33709bd8b8c8e41da4b61ab01eb50d188f532690520a6b69b6c4790d2076eebc32e01d59945b5c3d8af79d0b7eb271527f8c6eb6cf70bdd141a5278d6f9f557513ec56b94da27d7cb85117074d318154967e645f42b4b42231ad8e29f0a3ccd2596444f6cc1de903ec3cb27c28792e9437b6bc1cd57a61f15b96f1690027119cb87c07d96760230afff7f8c9287d0573c34830359694918a721d87213d0baba7ee2f519d839581
c = 0x40c4c7f7a326558762ac0f64a8abb6f6496851c45a2763791132ecc4c8e029cc0a8c9d6ddb62dbdedf1e4f2f8ba8cb8a965aa9eb8c88cd582274b6ba9402fa84e63a6847c925b3fc34c6d5e9b925f03c656b2a6c2691a15196e4a246c5e3cb46b41f5090bf588911fbd8459ca9da19c1a8f3cd61af905790dd049d16544a2c4fd38f99af62d8080d49b5760c86a0cdb94ddadc785415e4e3e5ddf413a0a10e919c3ddda9c571f26498312718b4da3063a294394dc01fbb2f2c514d2b70dd999980cf5743ecf843450d71a613d74a3ab5d201bf864a617c3a25fecb9191e0ebe9bf678abed2384deb5ce91f753e9f20036fe61edfada631a4876a5cca790bc46
e = 0x10001

# Pollard's p-1 algorithm: https://en.wikipedia.org/wiki/Pollard%27s_p_%E2%88%92_1_algorithm
B = 65535
p = -1
q = -1
while p == -1:
    b = fac(B)
    denom = gcd(n, pow(2, b, n) - 1)

    if denom == 1:
        B += 1
    elif denom == n:
        B -= 1
    else:
        p = denom
        q = n // p

# This is just RSA, see https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Operation
totient = (p - 1) * (q - 1)

d = pow(e, -1, totient)
m = pow(c, d, n)

flag = long_to_bytes(m)
print(flag)
