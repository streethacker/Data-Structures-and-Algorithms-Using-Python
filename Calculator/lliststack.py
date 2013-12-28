__author__ = "streethacker"

#-*- coding:utf-8 -*-
#/usr/bin/python

#Data Structures and Algorithms Using Python
#CHAPTER 7: Stacks
#Listing 7.2: lliststack.py

class _StackNode(object):
	def __init__(self, item, link):
		self.item = item
		self.next = link

class Stack:
	"""
	The front of the linked list(head) provides the most efficient representation for the top of
	the stack.Because it's quite easy to prepend nodes to the linked list as well as remove the 
	first node.
	"""
	def __init__(self):
		"""
		The constructor creates two instance variables for each Stack.The _top field is the head
		reference for maintaining the linked list while _size is an integer value for keeping tr
		ack of the number of items on the stack.The latter has to be adjusted when items are pus
		hed onto or popped off the stack.
		"""
		self._top = None
		self._size = 0

	def isEmpty(self):
		return self._top is None

	def __len__(self):
		return self._size

	def peek(self):
		"""
		The peek operation is only meant to examine the item on top of the stack.It should not be
		used to modify the top item as this would violate the definition of the Stack ADT.
		"""
		assert not self.isEmpty(), "Cannot peek at an empty stack."
		return self._top.item

	def pop(self):
		assert not self.isEmpty(), "Cannot pop from an empty stack."
		node = self._top
		self._top = self._top.next
		self._size -= 1
		return node.item

	def push(self, item):
		self._top = _StackNode(item, self._top)
		self._size += 1

if __name__ == "__main__":
		pass
