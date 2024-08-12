isqrt :: Integral a => a -> a
isqrt = floor . sqrt . fromIntegral

sumOfDigs :: Integral x => x -> x
sumOfDigs 0 = 0
sumOfDigs x = (x `mod` 10) + (sumOfDigs $ x `div` 10)

digitPowerSumSeq = [b^e | e <- [2..100], b <- [2..100], (sumOfDigs (b^e)) == b]

main = let index = 30 in
    print $ digitPowerSumSeq !! (index - 1)
