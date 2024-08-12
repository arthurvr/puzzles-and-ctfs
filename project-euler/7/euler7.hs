primes :: [Integer]
primes = [2, 3] ++ sieve (tail primes) [5,7..]
    where sieve (p:ps) xs = h ++ sieve ps [x | x <- t, rem x p /=0]
        where (h, ~(_:t)) = span(< p*p) xs

main :: IO ()
main = do
    print $ primes !! 10000
