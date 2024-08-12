main = putStrLn . show $ (sum [a^a | a <- [1..1000]]) `mod` 10^10
