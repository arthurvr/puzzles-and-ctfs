import System.IO
import Control.Monad
import Data.Char (ord)

isqrt :: Int -> Int
isqrt = floor . sqrt . fromIntegral

is_square :: Int -> Bool
is_square n = sq * sq == n
    where sq = isqrt n

-- From the given formula it follows that a number a triangle number iff (8n+1) is a perfect square.
is_triangle_num :: Int -> Bool
is_triangle_num n = is_square $ 8 * n + 1

word_value :: String -> Int
word_value s = sum $ map alphabetvalue s
    where alphabetvalue ch = (ord ch) - 64

is_triangle_word :: String -> Bool
is_triangle_word = is_triangle_num . word_value

wordsWhen :: (Char -> Bool) -> String -> [String]
wordsWhen p s =  case dropWhile p s of "" -> []
                                       s' -> w : wordsWhen p s''
                                            where (w, s'') = break p s'

main :: IO ()
main = do
    handle <- openFile "words.txt" ReadMode
    contents <- hGetContents handle

    let givenWords = map (filter (not . (`elem` "\"\n"))) $ wordsWhen (== ',') contents
     in print . length $ filter is_triangle_word givenWords
