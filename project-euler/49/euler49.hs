-- It works for now, but a better primality test would make this a lot more efficient. A probablistic
-- one, like Miller–Rabin, comes to mind.
isPrime n = (==2) $ length [i | i <- [1..n], n `mod` i == 0]

digits :: Integral x => x -> [x]
digits 0 = []
digits x = digits (x `div` 10) ++ [x `mod` 10]

qsort :: Ord a => [a] -> [a]
qsort []     = []
qsort (p:xs) = qsort lesser ++ [p] ++ qsort greater
    where lesser  = filter (< p) xs
          greater = filter (>= p) xs

sameDigits :: Integral x => x -> x -> Bool
sameDigits n m = qsort (digits n) == qsort (digits m)

main :: IO ()
main = do
    print [ (a,b,c) | a <- fourDigitPrimes, b <- dropWhile (<= a) fourDigitPrimes,
        sameDigits a b, let step = b - a, let c = b + step, sameDigits b c, c `elem` fourDigitPrimes ]
    where fourDigitPrimes = filter isPrime [1000..9999]
