<?php

function printLoadingBar($percentage) {
  $fullLoadingBar = 10;

  print "[";

  for ($i = 1; $i <= $percentage; $i++) {
    print "#";
  }

  for ($i = $percentage+1; $i <= $fullLoadingBar; $i++) {
    print " ";
  }

  print "]";

  print " " . $percentage . "0 %";
  print "\n";
}

// user input
$userInput = (int)readline("Enter a percentage:");
printLoadingBar($userInput);
