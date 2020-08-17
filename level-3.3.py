def decomposingChemicals(m):
	#The process for finding the probability of each state of a matrix is to solve the following
	#equation: FS = IS(I - A)^-1
	#where FS is the Final State probability vector, IS is the initial state vector
	#I is the identity matrix, A is the concerned matrix converted so all rows add to one (1),
	#and ^-1 is the inverse.

	#I will be using numpy to handle matrix inversion and multiplication.
	#I will be using fractions.Fraction to put the answer in the correct format.

	def convert(matrix):
		#This function is to take any given matrix and convert it so that each row sums to 1
		newMatrix = []

		for row in matrix:
			rowSum = float(sum(row))
			newRow = []
			if rowSum > 0:
				for value in row:
					newRow.append(value/rowSum)
			else:
				for value in row:
					newRow.append(0)
			
			newMatrix.append(newRow)

		return newMatrix

	def subtractFromIdentity(matrix):
		newMatrix = []

		for i in range(0,len(matrix)):
			newRow = []
			for j in range(0,len(matrix)):
				if i == j :
					newRow.append(1 - matrix[i][j])
				else:
					newRow.append(-1*matrix[i][j])
			
			newMatrix.append(newRow)

		return newMatrix


	def getInverse(matrix):
		return np.linalg.inv(np.array(matrix))

	def getInitialStateVector(matrixSize):
		stateVector = [1] #Row zero will always be the initial state for this problem.

		for i in range(1, matrixSize):
			stateVector.append(0)

		return stateVector

	def convertToFinalFormat(originalMatrix,solutionVector):
		asFraction = []
		denoms = []

		for index in range(0,len(originalMatrix)):
			if sum(originalMatrix[index]) == 0: #if it is a terminal state
				asFraction.append(Fraction(solutionVector[index]).limit_denominator())

		for fraction in asFraction:
			denoms.append(fraction.denominator)

		lcm = np.lcm.reduce(denoms)

		finalFormat = []
		for fraction in asFraction:
			temp = lcm/fraction.denominator
			finalFormat.append(fraction.numerator*temp)

		finalFormat.append(lcm)

		return finalFormat


	#First convert the array; then subtract from identity; then get the inverse
	manipulatedMatrix = getInverse(subtractFromIdentity(convert(m)))

	#Then get initialStateVector
	initialStateVector = getInitialStateVector(len(m))

	probabilityOfFinalStates = np.matmul(initialStateVector,manipulatedMatrix)

	return convertToFinalFormat(m,probabilityOfFinalStates)