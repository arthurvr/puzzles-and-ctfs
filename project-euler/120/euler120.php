<?php

// I used the binomial theorem to expand the given formula:
// https://en.wikipedia.org/wiki/Binomial_theorem
//
// There, a lot of terms are clear multiples of a^2, meaning we don't have to count them
// because of the modulo operation. After making a clear distinction between cases for
// even n and odd n, you see that the result is always n for even n. For odd n:
//
// r = 2na mod a^2 = 2n mod a
//
// Which is maximal when 2n is closest to a.
//   <=> 2n = a-1
//   <=> n = floor((a-1) / 2)
//
// Which makes for r_max = 2*a*n_max = 2 * a * floor((a-1) / 2)
function r_max(int $a): int {
	return 2 * $a * floor(($a - 1) / 2);
}


$sum = 0;
for ($i = 3; $i <= 1000; $i++) {
	$sum += r_max($i);
}
echo $sum;
