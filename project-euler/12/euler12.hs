import Data.List

primes = 2 : filter (null . tail . primeFactors) [3,5..]

primeFactors n = factor n primes
    where factor n (p:ps)
            | p*p > n = [n]
            | n `mod` p == 0 = p : factor (n `div` p) (p:ps)
            | otherwise = factor n ps

triangleNumbers = map (\n -> n * (n + 1) `div` 2) [1..]
divisors n = product $ map (\n -> (length n) + 1) (group (primeFactors n))

main = print . head $ filter ((> 500) . divisors) triangleNumbers

