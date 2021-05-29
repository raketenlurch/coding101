<?php

// Logische Lösung
function printMatrixRandomCharacter($number) {
  $digitsOfSquare = $number * $number;
  $randomNumber = rand(1, $digitsOfSquare);

  for ($i = 1; $i <= $digitsOfSquare; $i++) {
    if ($i == $randomNumber) {
      print "*";
    } else {
      print "#";
    }

    if ($i % $number == 0) {
      print "\n";
    }
  }
}

$userInput = (int)readline("Enter a number:");
printMatrixRandomCharacter($userInput);

// Mathematische Lösung
/*
public Vector3Int[] getGridCoordinatesForItem(Vector3Int pos, int item)
    {
        Vector2Int size = availableGridElements[item].size;
        Vector3Int[] allPositions = new Vector3Int[size.x * size.y];

        for (int i = 0; i < allPositions.Length; i++)
        {
            int x = i % size.x;
            int y = Mathf.FloorToInt(i / size.x);

            // 2D size VS on the grid VS world....
            allPositions[i] = new Vector3Int(pos.x + x, pos.y, pos.z - y);
        }

        return allPositions;
    }
*/
