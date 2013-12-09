__author__ = "streethacker"

#/usr/bin/python
#-*- coding:utf-8 -*-

#Data Structures and Algorithms Using Python
#CHAPTER 5: Searching and Sorting(basic/primary sorting)
#Listing 5.4: binsearch.py


def binarySearch(theRef, target):
	low, high = 0, len(theRef) - 1

	while low <= high:
			mid = (low + high) / 2
			if theRef[mid] == target:
					return mid
			elif target < theRef[mid]:
					high = mid - 1
			else:
					low = mid + 1

	return 	None


if __name__ == "__main__":
		case1 = [1, 2, 3, 10, 12, 22, 89, 100]
		case2 = [3, 10, 22, 23, 77, 87, 90, 101]
		case3 = [0, 1, 5, 7, 10, 33, 42, 56]
		case4 = [10, 10, 22, 29, 54, 77, 90, 100]

		print "The target index of case1 is: %s" % binarySearch(case1, 10)
		print "The target index of case2 is: %s" % binarySearch(case2, 10)
		print "The target index of case3 is: %s" % binarySearch(case3, 10)
		print "The target index of case4 is: %s" % binarySearch(case4, 10)
