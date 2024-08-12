-- I implemented the prime sieve from this tutorial, which seems quite efficient:
-- https://doisinkidney.com/posts/2018-11-10-a-very-simple-prime-sieve.html
-- All credits for this sieve go to the author :)

infixr 5 :-
data Queue a b = Queue { minKey :: !a, minVal :: b, rest   :: List a b }

data List a b = Nil | (:-) !(Queue a b) (List a b)

(<+>) :: Ord a => Queue a b -> Queue a b -> Queue a b
(<+>) q1@(Queue x1 y1 ts1) q2@(Queue x2 y2 ts2)
  | x1 <= x2 = Queue x1 y1 (q2 :- ts1)
  | otherwise = Queue x2 y2 (q1 :- ts2)

mergeQs :: Ord a => List a b -> Queue a b
mergeQs (t :- ts) = mergeQs1 t ts
mergeQs Nil       = errorWithoutStackTrace "tried to merge empty list"

mergeQs1 :: Ord a => Queue a b -> List a b -> Queue a b
mergeQs1 t1 Nil              = t1
mergeQs1 t1 (t2 :- Nil)      = t1 <+> t2
mergeQs1 t1 (t2 :- t3 :- ts) = (t1 <+> t2) <+> mergeQs1 t3 ts

insert :: Ord a => a -> b -> Queue a b -> Queue a b
insert !k !v = (<+>) (singleton k v)

singleton :: a -> b -> Queue a b
singleton !k !v = Queue k v Nil

primes = 2 : sieve 3 (singleton 4 2)
  where
    adjust !x q@(Queue y z qs) | x < y = q
                               | otherwise = adjust x (mergeQs1 (singleton (y + z) z) qs)
    sieve !x q | x < minKey q = x : sieve (x + 1) (insert (x * x) x q)
               | otherwise = sieve (x + 1) (adjust x q)

-- ... and a good prime sieve makes this solution quite straight forward!
--
-- I'm convinced I'd be able to simplify the `r` formula to something more efficient... but this is quite fast so I didn't bother.
main :: IO ()
main = do
    print . fst . head . filter ((>10^10) . r) $ zip [2..] primes
    where r (n, p) = ((p-1)^n + (p+1)^n) `mod` p^2

