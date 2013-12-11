__author__ = "streethacker"

#/usr/bin/python
#-*- coding:utf-8 -*-

#Data Structures and Algorithms Using Python
#CHAPTER 6: Linked Structures
#Lising 6.5: sorted linklistbag.py

from linklistbag import Bag

class _BagListNode:
	"""
	Defines a private storage class for creating list nodes. There are
	only two attributes: data field and next reference field.
	"""
	def __init__(self, data):
		self.data = data
		self.next = None

class sortedBag(Bag):
	"""
	A new implementation of Bag ADT. A small modification has been made to
	the data structure, that is, instead of using a common linked list, we
	use the sorted linked list this time.

	Some of the implementation of the methods such as __init__() method can
	simply be inherited from the Bag class, wheras some others cannot. As a
	result, we rewrite the following methods.
	"""
	def __contains__(self, target):
		"""
		Taking the advantage of a sorted linked list, we can teminate the linear
		search when we come into the first element which is larger than the targ
		-et. This would do no improvement to the cost of worst case but may redu
		-ce the cost of the average case.
		"""
		curNode = self._head
		while curNode is not None and curNode.data <= target:
				if curNode.data == target:
						return True
				else:
						curNode = curNode.next

		return False
	
	def add(self, data):
		"""
		Much unlike the previous implementation of the Bag ADT using unsorted
		linked list. When adding elements to a sorted linked list, we must fi
		-nd out the suitable position to insert at first so that the order of
		the linked list would be maintained.
		"""
		preNode = None
		curNode = self._head

		while curNode is not None and curNode.data < data:
				preNode = curNode
				curNode = curNode.next

		newNode = _BagListNode(data)

		if curNode is self._head:
				newNode.next = self._head
				self._head = newNode
		else:
				newNode.next = preNode.next
				preNode.next = newNode

		self._size += 1

	
	def remove(self, data):
		"""
		The only modification made to this method is that we can make sure
		the existence of the data to be removed more fast.
		"""
		preNode = None
		curNode = self._head

		while curNode is not None and curNode.data <= data:
				if curNode.data == data:
						if curNode is self._head:
								self._head = curNode.next
						else:
								preNode.next = curNode.next

						self._size -= 1

						return curNode.data
				else:
						preNode = curNode
						curNode = curNode.next


		raise AttributeError, "The item must be in the bag."



if __name__ == "__main__":
		bag = sortedBag()

		bag.add(10)
		bag.add(12)
		bag.add(36)
		bag.add(77)

		bag.printBagElements()

		#print
		#print len(bag)

		bag.remove(10)

		print 

		bag.printBagElements()

		#print	
		#print len(bag)

		#bag.remove(100)

	
