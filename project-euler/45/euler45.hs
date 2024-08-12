import Data.List (find)

isInt :: (RealFrac a) => a -> Bool
isInt x = x == (fromInteger $ round x)

isPentagonal :: Double -> Bool
isPentagonal t = isInt $ ((sqrt $ 24 * t + 1) + 1) / 6

-- Every other triangle number is a hexagonal number
-- https://en.wikipedia.org/wiki/Hexagonal_number
hexagonals :: [Double]
hexagonals = [1/2 * n * (n + 1) | n <- [1,3..]]

main = putStrLn . show . find (> 40755) $ [n | n <- hexagonals, isPentagonal n]
