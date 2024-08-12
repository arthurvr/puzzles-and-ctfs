<?php

/*
 * Complete the 'pairs' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER k
 *  2. INTEGER_ARRAY arr
 */

function pairs($k, $arr) {
    $result = 0;
    
    foreach($arr as $i => $valuei) {
        for ($j = $i; $j < sizeof($arr); $j++) {
            if (abs($valuei - $arr[$j]) == $k) {
                $result += 1;
            }
        }
    }
    
    return $result;
}

$fptr = fopen(getenv("OUTPUT_PATH"), "w");

$first_multiple_input = explode(' ', rtrim(fgets(STDIN)));

$n = intval($first_multiple_input[0]);

$k = intval($first_multiple_input[1]);

$arr_temp = rtrim(fgets(STDIN));

$arr = array_map('intval', preg_split('/ /', $arr_temp, -1, PREG_SPLIT_NO_EMPTY));

$result = pairs($k, $arr);

fwrite($fptr, $result . "\n");

fclose($fptr);
