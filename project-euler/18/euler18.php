<?php

$triangle = json_decode(file_get_contents('triangle.json'));

$memory = [];

function maxValue($r, $c) {
	global $triangle, $memory;

	if (array_key_exists($r, $memory) && array_key_exists($c, $memory[$r])) {
		return $memory[$r][$c];
	}

	if ($r == count($triangle) - 1) {
		return $triangle[$r][$c];
	}

	$optionA = maxValue($r + 1, $c);
	$optionB = maxValue($r + 1, $c + 1);
	$memory[$r][$c] = $triangle[$r][$c] + ($optionA > $optionB ? $optionA : $optionB);

	return $memory[$r][$c];
}

echo maxValue(0, 0);
