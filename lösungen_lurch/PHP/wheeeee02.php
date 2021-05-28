<?php

function duplicateHashtag($amount) {
	$hashtags = '';
	for ($i = 0; $i < $amount; $i++) {
		$hashtags .= "#";
	}

	return $hashtags;
}


// user input
$number = (int)readline("Enter MAX:");

$result = '';

for ($i = 1; $i <= $number; $i++) {
	$result = duplicateHashtag($i);
	print $result;
	print "\n";
}

for ($i = $number-1; $i >= 1; $i--) {
	$result = duplicateHashtag($i);
	print $result;
	print "\n";
}
