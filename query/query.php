<?php

function query($query) {
	$sql = mysql_query($query); // execute query
	if (mysql_errno()) { // errors?
		$backtrace = debug_backtrace();
		die($backtrace[0]['line'].' '.$backtrace[0]['file'].' '.mysql_error());
	} else {
		return $sql; // no errors → return reference object
	}
}

?>
