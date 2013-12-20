__author__ = "streethacker"

#/usr/bin/python
#-*- coding:utf-8 -*-

#Data Structures and Algorithms Using Python
#CHAPTER 7: Stacks
#Listing 7.1: pyliststack.py

class Stack(object):
	"""
	Implementation of Stack ADT based on Py's list.
	For the most efficient ordering, we let the end of the list represent the top of the stack and the front
	represent the base.As the stack grows,items are appended to the end of the list and when items are poppe
	d,they are removed from the same end.
	"""
	def __init__(self):
		self._stackItems = list()

	def __len__(self):
		return len(self._stackItems)

	def isEmpty(self):
		return True if len(self) == 0 else False

	def peek(self):
		"""
		Returns a reference to the item on top of a non-emtpy stack without removing it.
		Peeking, which cannot be done on an empty stack,does not modify the stack conten
		ts.
		"""
		assert len(self) > 0, "Cannot peek at empty stack."
		return self._stackItems[-1]

	def pop(self):
		"""
		Removes and returns the top item of the stack, if the stack is not empty. Items cannot
		be popped from an empty stack. The next item on the stack becomes the new top item.
		"""
		assert len(self) > 0, "Cannot pop at empty stack."
		return self._stackItems.pop()

	def push(self,item):
		"""
		Adds the given item to the top of the stack.
		"""
		return self._stackItems.append(item)

	def printStack(self):
		print "The snapshot of the items in the stack:"
		for item in self._stackItems:
				print item,
		print

if __name__ == "__main__":
		stack = Stack()
		for i in range(10):
				stack.push(i)

		if not stack.isEmpty():
				stack.printStack()

		for i in range(5):
				stack.pop()

		if not stack.isEmpty():
				stack.printStack()

		topVal = stack.peek()

		print "The top value of the stack right now is:", topVal


