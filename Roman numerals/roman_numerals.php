<?php

function roman($input) {
	$vals  = array(1000, 500, 100, 50, 10, 5, 1, 'M' => 1000, 'D' => 500, 'C' => 100, 'L' => 50, 'X' => 10, 'V' => 5, 'I' => 1);
	$chars = array('M', 'D', 'C', 'L', 'X', 'V', 'I');
	
	if (is_numeric($input) && ($input < 1 || $input > 3999)) {
		return false;
	}
	if (!is_numeric($input) && !preg_match('/[MDCLXVI]+/i', $input)) {
		return false;
	}
	
	if (is_numeric($input)) {
		$str = '';
		
		for ($x = 0; $x < 7; $x++) {
			
			$am     = floor($input / $vals[$x]);
			$input %= $vals[$x];
			
			if ($am == 4) { // max is 3 of same
				if (isset($lastChar) && (($lastChar == 'V' && $x == 6) || ($lastChar == 'L' && $x == 4) || ($lastChar == 'D' && $x == 2))) {
				 	// trying to make 9__
					$str  = substr($str, 0, -1).$chars[$x].$chars[($x-2)]; // remove last
				} else { // 4__
					$str .= $chars[$x].$chars[($x-1)];
				}
				$lastChar = $chars[$x];
			} elseif ($am > 0) {
				for ($y = 0; $y < $am; $y++) { // add the chars
					$str .= $chars[$x];
				}
				$lastChar = $chars[$x]; // save last for next loop
			}
		
		}
		return $str;
	} else {
		$input   = strtoupper($input);
		$arr     = str_split($input);
		$lastVal = 0;
		$num     = 0;
		
		foreach ($arr as $char) {
			$num += $vals[$char];
			if ($vals[$char] > $lastVal) { // trying to deduct (ex. XC -> 90)
				$num -= (2 * $lastVal); // remove added before this loop AND deduct
			}
			$lastVal = $vals[$char];
		}
		return $num;
	}
	
}

?>
