__author__ = "streethacker"

#/usr/bin/python
#-*-coding:utf-8-*-

#Data Structures and Algorithms Using Python
#CHAPTER 1: Abstract Data Tpyes
#The Bag Abstract Data Type: List-Based Implementation
#Listing 1.3/Listing 1.4

class _BagIterator:
	"""
	An iterator for the Bag ADT implemented as a Python list.

	+--------------------------------------------------------------+
	The following code segment illustrates how Python actually per-
	forms the iteration when a for loop is used with an instance of 
	the Bag class:

	#Create a BagIterator object for myBag.
	iterator = myBag.__iter__()

	#Repeat the while loop until break is called.
	while True:
			try:
				#Get the next item from the bag.If there are no more
				#items, the StopIteration exception is raised.
				item = iterator.__next__()

				#Perform the body of the for loop
				print item

			#Catch the exception and break from the loop when we are
			#done.
			except StopIteration:
				break
	+---------------------------------------------------------------+
	"""
	def __init__(self, theList):
		self._bagItems = theList
		self._curItems = 0

	def __iter__(self):
		return self

	def __next__(self):
		if self._curItems < len(self._bagItems):
				item = self._bagItems[self._curItems]
				self._curItems += 1
				return item
		else:
				raise StopIteration

class Bag:
	"""
	Implements the Bag ADT container using a Python list.
	"""

	#Constructs an empty bag.
	def __init__(self):
		self._theItems = list()

	#Returns the number of items in the bag.
	def __len__(self):
		return len(self._theItems)

	#Determines if an item is contained in the bag.
	def __contains__(self, item):
		return item in self._theItems

	#Adds a new item to the bag.
	def add(self, item):
		self._theItems.append(item)

	#Removes and returns an instance of the item from the bag.
	def remove(self, item):
		assert item in self._theItems, "The item must be in the bag"
		ndx = self._theItems.index(item)
		return self._theItems.pop(ndx)

	#Returns an iterator for traversing the list of items.
	def __iter__(self, item):
		return _BagIterator(self._theItems)
