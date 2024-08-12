digits :: Integral x => x -> [x]
digits 0 = []
digits x = digits (x `div` 10) ++ [x `mod` 10]

qsort :: Ord a => [a] -> [a]
qsort [] = []
qsort (p:xs) = qsort lesser ++ [p] ++ qsort greater
    where lesser  = filter (< p) xs
          greater = filter (>= p) xs

sameDigits :: Integral x => x -> x -> Bool
sameDigits n m = qsort (digits n) == qsort (digits m)

main = print . head $ filter isSolution [1..]
    where isSolution n = all (sameDigits n) [2*n,3*n,4*n,5*n,6*n]
