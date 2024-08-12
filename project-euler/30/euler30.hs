import Data.Char (digitToInt)

digits :: Int -> [Int]
digits n = map digitToInt (show n)

digitsPow :: Int -> Int -> [Int]
digitsPow p n = map (^p) (digits n)

main = do
    print $ sum [x | x <- [2..limit], (sum . digitsPow 5 $ x) == x]
        where limit = 9^5 * 6
