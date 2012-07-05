<?php

function pythagoras($a, $b, $c = null, $y = null, $d = false) {
	if ($a == null) {
		return sqrt(pow($c, 2) - pow($b, 2));
	} elseif ($b == null) {
		return sqrt(pow($c, 2) - pow($a, 2));
	} elseif ($c == null && $y == null) {
		return sqrt(pow($a, 2) + pow($b, 2));
	} elseif ($d) {
		return sqrt(pow($a, 2) + pow($b, 2) + pow($c, 2));
	} elseif ($y == null) {
		return (acos((pow($a, 2) + pow($b, 2) - pow($c, 2)) / (2 * $a * $b)) * 180 / pi());
	} elseif ($c == null && $y != null) {
		return sqrt(pow($a, 2) + pow($b, 2) - 2 * $a * $b * cos($y * pi() / 180));
	} else {
		return false;
	}
}

?>
