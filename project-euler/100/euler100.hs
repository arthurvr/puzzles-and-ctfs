main :: IO ()
main = do
    print . (+1) . fst . head . filter solutionSize $ iterate nextPair initialPair

    where initialPair = (14, 20)
          -- This formula follows from the integer solutions of the diophantine equation that follows from
          -- a/b * (a-1)/(b-1) = 1/2
          nextPair (x, y) = (3 * x + 2 * y + 2, 4 * x + 3 * y + 3)
          solutionSize (x, y) = y >= 10^12
