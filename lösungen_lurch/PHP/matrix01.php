<?php

function printMatrix($number) {
  for ($i = 1; $i <= $number; $i++) {
    for ($j = 1; $j <= $number; $j++) {
      print "#";
    }
    print "\n";
  }
}

printMatrix(5);
