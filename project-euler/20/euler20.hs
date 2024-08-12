import Data.Char (digitToInt)

factorial :: Integer -> Integer
factorial n = product [1..n]

digits :: Integer -> [Int]
digits n = map digitToInt (show n)

main = do
    print . sum . digits $ factorial 100
