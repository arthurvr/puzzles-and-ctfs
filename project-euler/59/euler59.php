<?php

$ciphertext = array_map('intval', fgetcsv(fopen('ciphertext.txt', 'r')));
$alphas = range('a', 'z');

function decrypt($key) {
	global $ciphertext;

	$extended_key_str = str_repeat($key, intdiv(count($ciphertext), 3) + 1);
	$extended_key = array_map('ord', str_split($extended_key_str));

	$plaintext = array();
	for($i = 0; $i < count($ciphertext); $i++) {
		array_push($plaintext, $ciphertext[$i] ^ $extended_key[$i]);
	}

	return join(array_map('chr', $plaintext));
}

function ascii_sum($str) {
	return array_sum(array_map('ord', str_split($str)));
}

// Lazy way to get all permutations :)
foreach ($alphas as $alpha1) {
	foreach ($alphas as $alpha2) {
		foreach ($alphas as $alpha3) {
			$key = $alpha1 . $alpha2 . $alpha3;
			$plaintext = decrypt($key);

			if (strpos($plaintext, ' and ') !== false) {
				echo ascii_sum($plaintext) . "\n";
			}
		}
	}
}
