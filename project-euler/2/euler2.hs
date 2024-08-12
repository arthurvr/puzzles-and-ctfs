fibs :: [Integer]
fibs = 1 : 2 : zipWith (+) fibs (tail fibs)

main = do
    print . sum . filter even . takeWhile (<4*10^6) $ fibs
