import Data.Ratio

-- A fraction like xy/yz = x/z
-- Results in (10x + y)/(10y+z) = x/z
--        <=> 9xz + yz = 10xy
--
-- Where, obviously, we choose x y and z only from the range R = [1..]
-- (Btw: look at how nice working with fractions in Haskell is!)

main :: IO ()
main = do
    print . denominator . product $ [(10*x+y) % (10*y+z) | x <- r, y <- r, z <- r, x /= y,
                                                     (9*x*z) + (y*z) == (10*x*y)]
        where r = [1..9]

