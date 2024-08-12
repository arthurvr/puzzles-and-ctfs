palindrome :: Eq a => [a] -> Bool
palindrome s = s == reverse s

digits :: Integer -> Integer -> [Integer]
digits _ 0 = []
digits base x = digits base (x `div` base) ++ [x `mod` base]

main = do
    print $ sum [x | x <- [1..10^6], palindrome (digits 10 x), palindrome (digits 2 x)]
