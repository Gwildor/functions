<?php

function irclog($q) {
	$q = explode("\n", preg_replace('/(\r\n|\r|\n)/', "\n", $q));
	foreach ($q as $key => $val) {
		$val = preg_replace('/(\s{2,})/', ' ', $val);
		if ($val[0] == ' ') {
			$val = substr($val, 1);
		}
		$q2 = explode(' ', $val);
		if ((is_numeric($q2[0][1]) && is_numeric($q2[0][2]) && $q2[0][3] == ':' && is_numeric($q2[0][4]) && is_numeric($q2[0][5])) || (is_numeric($q2[0][0]) && is_numeric($q2[0][1]) && $q2[0][2] == ':' && is_numeric($q2[0][3]) && is_numeric($q2[0][4]))) { // time with () stuff
			$q2[0] = '['.str_replace(array('[', ']', '(', ')'), '', $q2[0]).']';
			$p = 1;
		} else {
			$p = 0;
		}
		if ($q2[(0+$p)] != '*' && $q2[(0+$p)] != '•' && $q2[(0+$p)] != '€') {
			if ($q2[(0+$p)] == '·' && $q2[(2+$p)] == '·') {
				unset($q2[(0+$p)], $q2[(2+$p)]);
				$q2[(1+$p)] = '<'.str_replace(array('<', '>', '(', ')'), '', $q2[(1+$p)]).'>';
			} else {
				if ($q2[(1+$p)] == '›') {
					$q2[(1+$p)] = $q2[(0+$p)];
					$q2[(0+$p)] = '*';
				} else {
					if ($q2[(1+$p)] == '•') {
						unset($q2[(1+$p)]);
					}
					$q2[(0+$p)] = '<'.str_replace(array('<', '>', '(', ')'), '', $q2[(0+$p)]).'>';
				}
			}
		} else {
			$q2[(0+$p)] = '*';
		}
		$q[$key] = implode(' ', $q2);
	}
	
	return implode("\n", $q);
}

?>
