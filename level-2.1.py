def lambsDelivered(total_lambs):
	#given any integer total_lambs divide them in the most generous and stingy ways possible

	def generous(total_lambs):
		#do the generous calculation here
		#The generous calculation starts from 1 and doubles each time
		#I need to keep a sum of all the payments (doubled numbers)
		doubleStart = [1,1] #[startingValue,sumOfAllValues]
		paidHenchmen = 1 #We've only paid 1 henchman 1 lamb so far

		while doubleStart[1] < total_lambs:
			newDouble = doubleStart[0]*2
			doubleStart[0] = newDouble
			doubleStart[1] = doubleStart[1] + newDouble

			if doubleStart[1] <= total_lambs:
				paidHenchmen = paidHenchmen + 1

		return paidHenchmen


	def stingy(total_lambs):
		#I have noticed that the stingy payout rules can be satisfied through following the
		#fibonacci sequence.

		#Calculate fibonacci through keeping most recent 2 numbers
		#Also keep the total sum of fibonacci numbers - which must stay below (or equal to) total_lambs

		#This is an edge case that would be improperly handled starting from fibStart = [1,1,2]
		if total_lambs == 1:
			return 1

		fibStart = [1,1,2] #[fibX,fibX+1,fibSum]

		paidHenchmen = 2 #since the first 2 have already been accounted for.

		while fibStart[2] < total_lambs:
			nextFib = fibStart[0] + fibStart[1]
			fibStart[0] = fibStart[1]
			fibStart[1] = nextFib

			fibStart[2] = fibStart[2] + fibStart[1]

			if fibStart[2] <= total_lambs:
				paidHenchmen = paidHenchmen + 1

		return paidHenchmen

	
	#Handling the case of Zero Lambs outside of the generous and stingy functions
	if total_lambs == 0:
	    return 0
	else:
	    return stingy(total_lambs) - generous(total_lambs)
