<?php

$handle = fopen("words.txt", "r");
if ($handle) {
    while (($word = fgets($handle)) !== false) {
	$word = trim($word);

	if ((strlen($word) === 16) && (substr($word,6,1) == substr($word,10,1)) && (substr($word,14,1) == substr($word,10,1))) {
		echo $word . "\n";
	}
    }

    fclose($handle);
}
