def dontGetVolunteered(src,dest):
	#Given a src and dest input on an 8X8 chess board, find the shortest path from src to dest
	#using only Knight (chess) moves.

	#A way to make this optimal is to use a breadth first search algorithm.

	#This function is used to turn the src and dest given into an [X,Y] coordinate
	#This will make it easier to create the logic for "moving" around the board.
	def getCoordinates(space):
		chessboard = [[0,1,2,3,4,5,6,7],[8,9,10,11,12,13,14,15],[16,17,18,19,20,21,22,23],[24,25,26,27,28,29,30,31],\
			[32,33,34,35,36,37,38,39],[40,41,42,43,44,45,46,47],[48,49,50,51,52,53,54,55],[56,57,58,59,60,61,62,63]]

		coordinates = []

		for i in range(0,len(chessboard)):
			if space in chessboard[i]:
				coordinates = [chessboard[i].index(space),i] #[X,Y] Coords
		return coordinates

	#This takes a given [X,Y] position and returns a list of coordinates of all possible Knight moves
	def createPossibleMoves(position):
		possibleMoves = [[2,1],[2,-1],[1,2],[1,-2],[-2,1],[-2,-1],[-1,2],[-1,-2]]
		newPosition = position
		movesList = []
		for move in possibleMoves:
			newPosition = [position[0] + move[0],position[1] + move[1]]

			#Check if the new position is a legal position on the board
			if newPosition[0] >= 0 and newPosition[0] <= 7 and newPosition[1] >= 0 and newPosition[1] <= 7:
				movesList.append(newPosition)
		return movesList	

	#This finds the shortest path between src and dest using a breadth first search
	def findShortestPath(srcCoord, destCoord):
	    checked = []
	    pathsToCheck = [[srcCoord]]
	 
	    #Most Simple Case
	    if srcCoord == destCoord:
	        return [srcCoord,destCoord]
	 
	    #Checking all path options
	    while pathsToCheck:
	        currentPath = pathsToCheck.pop(0)
	        #Get the current position from the current path
	        position = currentPath[len(currentPath)-1]
	        if position not in checked:
	            nextMove = createPossibleMoves(position)
	            
	            #For each nextMove available create new path with nextMove appended.
	            for move in nextMove:
	                nextPath = list(currentPath)
	                nextPath.append(move)
	                pathsToCheck.append(nextPath)
	                
	                #If latest move reached destination then return path
	                if move == destCoord:
	                    return nextPath
	 
	            #Don't need to look at this space moving forward
	            checked.append(position)

	#First use getCoordinates() to turn the src and dest into [X,Y] positions
	srcCoord = getCoordinates(src)	
	destCoord = getCoordinates(dest)

	shortestPath = findShortestPath(srcCoord,destCoord)

	#shortestPath includes the starting point which is not a "step"
	#so the number of steps in the path will be len(shortestPath) - 1,
	#but there is two special cases when len(shortestPath) is 2 that
	#need to be handled.
	if len(shortestPath) == 2:
		if shortestPath[0] == shortestPath[1]:
			#src and dest were the same
			return 0
		else:
			#this was a one step path
			return 1
	else:
		return len(shortestPath) - 1
