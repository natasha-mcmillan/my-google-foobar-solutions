def cake(s):
	#Given a string S of any length, find the exact number of repeating substrings

	#I want the smallest pieces therefore I should count up.
	cakeSize = len(s)
	startingPoint = len(set(s)) #At a minimum the piece size must encorporate all diff M&Ms

	currentMost = 0

	#This checks if there is one M&M for the whole cake
	if len(set(s)) == 1:
		return cakeSize

	#This checks for patterns with any other number of M&Ms
	for testSize in range(startingPoint,cakeSize+1):
		if cakeSize%testSize == 0:
			#this shows potential for repeating pattern
			#from here create "chunks" and check for equality
			cakePieces = []
			cakePieces = [s[x:x+testSize] for x in range(0,len(s),testSize)]

			if(len(set(cakePieces)) == 1):
				currentMost = cakeSize/testSize if currentMost < cakeSize/testSize else currentMost

		testSize = testSize - 1

		#I briefly considered that checking the string as is may not be enough since the cake is
		#circular, but I could not find an example where this actually mattered.
		#Example: "abcabc" in a round could be "bcabca" or "cabcab" but ultimately the result is
		#the same, so I don't believe it matters.

	return currentMost