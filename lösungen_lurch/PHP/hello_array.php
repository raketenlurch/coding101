<?php

// Array
$pets = array('hamster', 'hund', 'katze', 'pferd');

$pets = ['hamster', 'hund', 'katze', 'pferd'];

for ($i = 0; $i < count($pets); $i++) {
  print $pets[$i] . "\n";
}

$pets[] = 'wurm';

print_r($pets);

$pets[1] = 'duck';

print_r($pets);

// PHP-"Magic"
$pets[42] = 'pidgeon';

print_r($pets);

$pets[] = 'opposum';

print_r($pets);

$pets[7] = 'drossel';

print_r($pets);

$pets[] = 'giraffe';

print_r($pets);

// Remove element from array
unset($pets[2]);

print_r($pets);

// Dictionary
$meals = ['breakfast' => 'croiassant', 'lunch' => 'pizza', 'dinner' => 'pasta'];

foreach ($meals as $key => $value) {
  print $key . ' ' . $value . "\n";
}

$meals['second dinner'] = 'apple';

print_r($meals);

$meals['lunch'] = 'pizza tonno';

print_r($meals);

// PHP-"Magic"
$meals[] = 'döner';

print_r($meals);

// Remove element from Dictionary
unset($meals['dinner']);

print_r($meals);

unset($meals[0]);

print_r($meals);
