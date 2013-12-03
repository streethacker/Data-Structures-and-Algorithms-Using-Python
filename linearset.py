__author__ = "streethacker"

#/usr/bin/python
#-*-coding:utf-8-*-

#Data Structures and Algorithms Using Python
#CHAPTER 3: Sets and Maps
#Listing 3.1: linearset.py

class _SetIterator:
	"""
	Iterator Class which is used to create a iterator object
	for traversing all the elements in a set structure one by
	one.
	"""
	def __init__(self, theSet):
		self._setRef = theSet
		self._curNdx = 0

	def __iter__(self):
		return self

	def next(self):
		if self._curNdx < len(self._setRef):
				item = self._setRef[self._curNdx]
				self._curNdx += 1
				return item
		else:
				raise StopIteration


class Set:
	"""
	A set stores unique values and represents the same structure
	found in mathematics. It is commonly used when you need to 
	store a collection of unique values without regard to how the
	-y are stored or when you need to perform various mathematical
	set operations on collections.

	A set is a container that stores a collection of unique values
	over a given comparable domain in which the stored values have
	no particular ordering.
	"""
	def __init__(self):
		self._theElements = list()

	def __len__(self):
		return len(self._theElements)

	def __contains__(self, element):
		return element in self._theElements

	def add(self, element):
		"""
		Modifies the set by adding the given value or element to the
		set if the element is not already a member. If the element is
		not unique, no action is taken and the operation is skipped.
		"""
		if element not in self._theElements:
				self._theElements.append(element)

	def remove(self, element):
		"""
		Removes the given value from the set if the valueis contained
		in the set and raises an exception otherwise.
		"""
		assert element in self._theElements, "The element must be in the set."
		self._theElements.remove(element)

	def __eq__(self, setB):
		"""
		Determines if the set is equal to another set and returns a bool
		-ean value. For two sets, A and B, to be equal, both A and B must
		contain the same number of elements and all elements in A must al
		-so be elements in B. If both sets are empty, the sets are equal.
		Access with == or !=.
		"""
		if len(self) != len(setB):
				return False
		else:
				return self.isSubsetOf(setB)

	def isEmpty(self):
		return True if len(self._theElements) == 0 else False

	def isSubsetOf(self, setB):
		"""
		Determines if the set is a subset of another set and returns a 
		boolean value. For set A to be a subset of set B, all elements
		in set A must also be elements in set B.
		"""
		for element in self:
				if element not in setB:
						return False
		return True

	def union(self, setB):
		"""
		Creates and returns a new set that is the union of this set and
		set B. The new set created from the union of two sets, A and B,
		contains all elements in A plus those elements in B that are not
		in A. Neither set A nor set B is modified by this operation.
		"""
		newSet = Set()
		newSet._theElements.extend(self._theElements)
		for element in setB:
				if element not in self:
						newSet._theElements.append(element)
		return newSet

	def intersection(self, setB):
		"""
		Creates and returns a new set that is the intersection of this
		set and set B. The intersection of set A and set B contains on
		-ly those elements that are in both A and B. Neither A nor B is 
		modified by this operation.
		"""
		newSet = Set()
		for element in setB:
				if element in self:
						newSet._theElements.append(element)
		return newSet
		
	def difference(self, setB):
		"""
		Creates and returns a new set that is the difference of this set
		and set B. The set difference, A-B, contains only those elements
		that are in A but not in B. Neither set A nor set B is modified 
		by this operation.
		"""
		newSet = Set()
		for element in self:
				if element not in setB:
						newSet._theElements.append(element)
						
	def __iter__(self):
		return _SetIterator(self._theElements)

if __name__ == "__main__":
	smith = Set()
	smith.add("CSCI-112")
	smith.add("MATH-121")
	smith.add("HIST-340")
	smith.add("ECON-101")

	roberts = Set()
	roberts.add("POL-101")
	roberts.add("ANTH-230")
	roberts.add("CSCI-112")
	roberts.add("ECON-101")

	if smith == roberts:
			print "Smith and Roberts are taking the same courses."
	else:
			sameCourses = smith.intersection(roberts)
			if sameCourses.isEmpty():
					print "Smith and Roberts are not taking any of the same courses."
			else:
					print "Smith and Roberts are taking some of the same courses:"
					for course in sameCourses:
							print course
