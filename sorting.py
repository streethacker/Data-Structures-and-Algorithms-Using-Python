def simpleBubbleSort(theRef):
	"""
	Sorts a sequence in ascending order using the simple bubble
	sort algorithm.

	The efficiency of the simple bubble sort algorithm only dep
	-ends on the number of keys in the array and is independent
	of the specific values and the initial arrangement of those
	values.

	Simple bubble sort is considered one of the most inefficient
	sorting algorithms due to the total number of swaps requierd.
	Even in the best case, the cost is still O(n^2).
	"""
	max = len(theRef) - 1

	for i in range(max):
			for j in range(max - i):
					if theRef[j] > theRef[j+1]:
							exchange = theRef[j] 
							theRef[j] = theRef[j+1]
							theRef[j+1] = exchange

	return 

def advancedBubbleSort(theRef):
	"""
	Almost the same as the simple bubble sort algorithm's performance
	in the worst case.
	The only improvement is that a 'swapFlg' is introced in. With the
	help of this label, we can determine the sequence is sorted order
	when no swaps are performed by the if statement within the inner l
	-oop. At that point, the function can return immediately without c
	-ompleting the remaining iterations. O(n) in the best case.
	"""
	max = len(theRef) - 1

	swapFlg = False

	for i in range(max):
			for j in range(max - i):
					if theRef[j] > theRef[j+1]:
							swapFlg = True
							exchange = theRef[j]
							theRef[j] = theRef[j+1]
							theRef[j+1] = exchange
			if swapFlg == False:
					break
	return

def selectionSort(theRef):
	"""
	The selection sort, which improves on the bubble sort, makes multiple
	passes over the sequence, but unlike the bubble sort, it onley makes a
	single swap after each pass(reduce the number of swap times to O(n)).

	O(n^2) in the worst case, still.
	"""
	max = len(theRef) - 1

	for i in range(max-1):
			smallIdx = i
			for j in range(i+1, len(theRef)):
					if theRef[j] < theRef[smallIdx]:
							smallIdx = j

			if smallIdx != i:
					exchange = theRef[i]
					theRef[i] = theRef[smallIdx]
					theRef[smallIdx] = exchange

	return

def insertionSort(theRef):
	"""
	The insertion sort maintains a collection of sorted items and a 
	collection of items to be sorted.
	
	When implementing insertion sort in a program, the algorithm mai
	-ntains both the sorted and unsorted collections within the same
	sequence structure. The algorithm keeps the list of sorted values
	at the front of the sequence and picks the next unsorted value fr
	-om the list of those yet to be positioned.

	O(n^2) in the best case, still.
	"""
	for i in range(1, len(theRef)):
			key = theRef[i]
			insertIdx = i

			while insertIdx > 0 and key < theRef[insertIdx-1]:
					theRef[insertIdx] = theRef[insertIdx-1]
					insertIdx -= 1

			theRef[insertIdx] = key
	
	return 


if __name__ == "__main__":
		testcase = [2, 3, 1, 10, 6, 30, 27]
		#simpleBubbleSort(testcase)
		#advancedBubbleSort(testcase)
		#selectionSort(testcase)
		insertionSort(testcase)
		print "Sorted list: %s" % testcase
