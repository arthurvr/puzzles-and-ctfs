factorial :: Integer -> Integer
factorial n = product [1..n]

choose :: Integer -> Integer -> Integer
choose a b = (factorial a) `div` ((factorial b) * (factorial (a - b)))

-- For every path, 20 horizontal 'moves' and 20 vertical ones need to be made. In total that's 40 steps.
-- Just need to count how many different ways there are of choosing which steps are horizontal and which are vertical.
main = do
    print $ choose 40 20
