<?php

$table = array(
	1 => "one",
	2 => "two",
	3 => "three",
	4 => "four",
	5 => "five",
	6 => "six",
	7 => "seven",
	8 => "eight",
	9 => "nine",
	10 => "ten",
	11 => "eleven",
	12 => "twelve",
	13 => "thirteen",
	14 => "fourteen",
	15 => "fifteen",
	16 => "sixteen",
	17 => "seventeen",
	18 => "eighteen",
	19 => "nineteen",
	20 => "twenty",
	30 => "thirty",
	40 => "forty",
	50 => "fifty",
	60 => "sixty",
	70 => "seventy",
	80 => "eighty",
	90 => "ninety"
);

function spell_number($num) {
	global $table;

	$result = "";

	if ($num == 1000) {
		return "onethousand";
	}

	$hundreds = intdiv($num, 100);
	$twoDigitQuotient = $num % 100;
	$tens = intdiv($twoDigitQuotient, 10);
	$units = $twoDigitQuotient % 10;

	if ($hundreds != 0) {
		$result .= $table[$hundreds] . "hundred";
	}

	if ($twoDigitQuotient != 0) {
		if($hundreds != 0) {
			$result .= "and";
		}

		if($twoDigitQuotient >= 1 && $twoDigitQuotient <= 19) {
			$result .= $table[$twoDigitQuotient];
		}
		else {
			$result .= $table[$tens * 10];

			if($units != 0) {
				$result .= $table[$units];
			}
		}
	}

	return $result;
}

$sum = 0;
for ($i = 1; $i <= 1000; $i++) {
	$sum += strlen(spell_number($i));
}

echo $sum;
