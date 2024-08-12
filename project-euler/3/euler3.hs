primeFactors :: Integer -> [Integer]
primeFactors n = factor n primes
    where factor n (x:xs) | x^2 > n = [n]
                          | n `mod` x == 0 = x : factor (n `div` x) xs
                          | otherwise = factor n xs
          primes = [2, 3] ++ filter ((==1) . length . primeFactors) [5,7..]

main :: IO ()
main = do
    print . last . primeFactors $ 600851475143
