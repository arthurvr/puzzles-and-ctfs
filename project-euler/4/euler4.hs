main = print . maximum $ [ab | a <- [1..999], b <- [1..999], let ab = a*b, (reverse $ show ab) == show ab]
