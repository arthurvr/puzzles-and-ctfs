import Data.Char (digitToInt)

digitSum = sum . map digitToInt . show
main = print $ digitSum (2^1000)
