def staircase(n):
	#If bricks is equal to X then the least amount of staircases we can build
	#is the amount we could build with X - 1 bricks. This information can be
	#used as the starting point for determining how many staircases X can make.

	#First make an empty list of lists to store the counts. This list must be of
	#size X + 1 by X + 1 to leave space for the base case (of zero).

	bricks = n

	currentSets = []

	for i in range(0, bricks + 1):
		temp = []
		for j in range(0, bricks + 1):
			temp.append(0)
		currentSets.append(temp)

	#If we currently have zero bricks and zero steps there is only "one" way to "build" a staircase.
	currentSets[0][0] = 1

	for lastStep in range(1, bricks + 1):
		for bricksLeft in range(0, bricks + 1):
			#By adding a brick we can create at least as many steps as we could with one less brick.
			currentSets[lastStep][bricksLeft] = currentSets[lastStep - 1][bricksLeft]

			#If we have more extra bricks than the height of the last step then we can create more staircases
			if bricksLeft >= lastStep:
				currentSets[lastStep][bricksLeft] = currentSets[lastStep][bricksLeft] + currentSets[lastStep - 1][bricksLeft - lastStep]

	#We must subtract 1 from the final result because our base case doesn't
	#actually qualify as a staircase.
	return currentSets[bricks][bricks] - 1

import numpy as np
from fractions import Fraction
