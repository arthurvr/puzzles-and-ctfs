main = do
    print $ sum [e | e <- [2..totient - 1], gcd e totient == 1, gcd (e - 1) (a - 1) == 2, gcd (e - 1) (b - 1) == 2]

    where totient = (a - 1) * (b - 1)

