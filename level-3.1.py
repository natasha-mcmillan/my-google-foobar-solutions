def findTheAccessCodes(l):
	#Checking each item in the list for multiples will be taxing for large lists
    #Instead I will create a dictionary for each index, of all the indexes which
    #contain values that are divisible by the key index's value.
    
    #For example l = [2,4,8,10,16]
    #Map of l = {0:[1,2,3,4],1:[2,4],2:[4],3:[],4:[]}
    #Then this can be counted by looping through the values of each key, and
    #adding the length of the second key's value list to the total.
    
    #Example with the above list: key 0 has 1 as a value and 1 has 2 items so
    #total = total + 2. key 0 has 2 as a value and 2 has 1 item so
    #total = total + 1. The remaining are zeros so in this case 3 is the final total.


	startingList = l

	def createMapping(startingList):

		divisibleDict = {}

		for i in range(0,len(startingList)-1):
			tempList = []
			for j in range(i+1,len(startingList)):
				if startingList[j] % startingList[i] == 0:
					tempList.append(j)
			divisibleDict[i] = tempList

		return divisibleDict

	def countFromMapping(myMapping):
		count = 0

		for key in myMapping:
			for value in myMapping[key]:
				if myMapping.get(value):
					count = count + len(myMapping.get(value))



		return count

	return countFromMapping(createMapping(startingList))
