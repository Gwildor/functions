<?php

function subsentence($str, $start, $length = null) {
	if ($length === false) {
		return '';
	}
	
	$arr = explode(' ', $str);
	$len = count($arr);
	
	// If string is less than or equal to start characters long, FALSE will be returned.
	if ($len <= $start) {
		return false;
	}
	
	if ($start < 0) {
		$start += $len;
	}
	
	if ($length === null) {
		$length = $len;
	} else {
		if ($length < 0) {
			$length += $len;
			
			// If start denotes the position of this truncation or beyond, false will be returned.
			if ($length <= $start) {
				return false;
			}
		} else {
			$length += $start;
		}
	}
	
	$str = '';
	for ($x = $start; $x < $length; $x++) {
		if (isset($arr[$x])) {
			$str .= ' '.$arr[$x];
		}
	}
	
	return substr($str, 1);
}

?>
