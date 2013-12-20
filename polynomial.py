__author__ = "streethacker"

#/usr/bin/python
#-*- coding:utf-8 -*-

#Data Structures and Algorithms Using Python
#CHAPTER 6: Linked Structures
#Listing 6.14: polynomial.py

class _PolyTermNode(object):
	"""
	The polynomial term node structure, which contains two main fields(actually three):
	degree: the degree of a single term of the polynomial
	coefficient: the coefficient of a single term of the polynomial.
	"""
	def __init__(self, degree, coefficient):
		self.degree = degree
		self.coefficient = coefficient
		self.next = None

class Polynomial:
	"""
	A polynomial is a mathematical expression of a variable constructed of one or more
	terms.Each term is of the form a_i*x^i where a_i is a scalar coefficient and x^i i
	s the unknown variable of degree i.
	"""

	def __init__(self, degree=None, coefficient=None):
		"""
		Using the technology of default parameters:
		i. Creates a new polynomial initialized to be empty and thus containing not terms.
		ii.Creates a new polynomial initialized with a single term constructed from the d
		egree and coefficient arguments.
		"""
		if degree is None:
				self._polyHead = None
		else:
				self._polyHead = _PolyTermNode(degree, coefficient)
		self._polyTail = self._polyHead

	def degree(self):
		"""
		Returns the degree of the polynomial(not a term, that is, the largest degree of all the
		terms).If the polynomial contains no terms, a value of -1 is returned.
		"""
		if self._polyHead is None:
				return -1
		else:
				return self._polyHead.degree

	def __getitem__(self, degree): 
		"""
		Returns the coefficient for the term of the provided degree. Thus,if the expression of
		this polynomial is x^3 + 4x + 2 and a degree of 1 is provided, this operation returns 4.
		The coefficient cannot be returned for an empty po
		Returns the coefficient for the term of the provided degree. Thus,if the expression of
		this polynomial is x^3 + 4x + 2 and a degree of 1 is provided, this operation returns 4.
		The coefficient cannot be returned for an empty polynomial.
		"""
		assert self.degree() >= 0, \
			"Operation not permitted on an empty polynomial."

		curNode = self._polyHead
		while curNode is not None and curNode.degree >= degree:
				curNode = curNode.next

		if curNode is None or curNode.degree != degree:
				return 0.0
		else:
				return curNode.coefficient

	def evaluate(self, scalar):
		"""
		Evaluates the polynomial at the given scalar value and returns the result. An empty
		polynomial cannot be evaluated.
		"""
		assert self.degree >= 0, \
			"Only non-empty polynomials can be evaluated."

		result = 0.0

		curNode = self._polyHead
		while curNode is not None:
				result += curNode.coefficient*(scalar ** curNode.degree)
				curNode = curNode.next

		return result

	def __add__(self, rhsPoly):
		"""
		Creates and returns a new Polynomial that is the result of adding this polynomial and
		the rhsPoly.This operation is not defined if either polynomial is empty.
		"""
		assert self.degree() >= 0 and rhsPoly.degree() >= 0, \
			"Addition only allowed on non-empty polynomials."

		newPoly = Polynomial()
		nodeA = self._polyHead
		nodeB = rhsPoly._polyHead

		while nodeA is not None and nodeB is not None:
				if nodeA.degree > nodeB.degree:
						degree = nodeA.degree
						coefficient = nodeA.coefficient
						nodeA = nodeA.next
				elif nodeA.degree < nodeB.degree:
						degree = nodeB.degree
						coefficient = nodeB.coefficient
						nodeB = nodeB.next
				else:
						degree = nodeA.degree #or degree = nodeB.degree
						coefficient = nodeA.coefficient + nodeB.coefficient
						nodeA = nodeA.next
						nodeB = nodeB.next

				newPoly._appendTerm(degree, coefficient)

		while nodeA is not None:
				newPoly._appendTerm(nodeA.degree, nodeA.coefficient)
				nodeA = nodeA.next

		while nodeB is not None:
				newPoly._appendTerm(nodeB.degree, nodeB.coefficient)
				nodeB = nodeB.next

		return newPoly

	def __sub__(self, rhsPoly):
		"""
		Almost the same as the __add__() method, whearas when the nodeA's degree is smaller than the nodeB's
		degree, the new coefficient will be the -nodeB.coefficient.
		"""
		assert self.degree() >= 0 and rhsPoly.degree() >= 0, \
			"Substraction only allowed on non-empty polynomials."

		newPoly = Polynomial()
		nodeA = self._polyHead
		nodeB = rhsPoly._polyHead

		while nodeA is not None and nodeB is not None:
				if nodeA.degree > nodeB.degree:
						degree = nodeA.degree
						coefficient = nodeA.coefficient
						nodeA = nodeA.next
				elif nodeA.degree < nodeB.degree:
						degree = nodeB.degree
						coefficient = -nodeB.coefficient  #-nodeB.coefficient
						nodeB = nodeB.next
				else:
						degree = nodeA.degree	#or degree = nodeB.degree
						
						#cannot exchange A and B's position
						coefficient = nodeA.coefficient - nodeB.coefficient
						nodeA = nodeA.next
						nodeB = nodeB.next

				newPoly._appendTerm(degree, coefficient)

		while nodeA is not None:
				newPoly._appendTerm(nodeA.degree, nodeA.coefficient)
				nodeA = nodeA.next

		while nodeB is not None:
				newPoly._appendTerm(nodeB.degree, nodeB.coefficient)
				nodeB = nodeB.next

		return newPoly

	def __mul__(self, rhsPoly):
		"""
		Computing the product of two polynomials requires multiplying the second polynomial by each term.This
		generates a series of intermediate polynomials, which are then be added to create the final product.
		"""
		assert self.degree() >= 0 and rhsPoly.degree() >= 0,\
			"Multiplication only allowed on non-empty polynomials."

		node = self._polyHead
		newPoly = rhsPoly._termMultiply(node)

		node = node.next
		while node is not None:
				tempPoly = rhsPoly._termMultiply(node)
				newPoly += tempPoly
				node = node.next

		return newPoly

	def _termMultiply(self, termNode):
		"""
		Helper method which creates a new polynomial from multiplying an existing polynomial by another term.
		"""
		newPoly = Polynomial()

		curr = self._polyHead
		while curr is not None:
				newDegree = curr.degree + termNode.degree
				newCoefficient = curr.coefficient * termNode.coefficient

				newPoly._appendTerm(newDegree, newCoefficient)

				curr = curr.next

		return newPoly

	def _appendTerm(self, degree, coefficient):
		"""
		Helper method which accepts the degree and coefficient of a polynomial term, creates a new node to store the term
		and appends the node to the end of the list.
		"""
		if coefficient != 0.0:
				newTerm = _PolyTermNode(degree, coefficient)
				if self._polyHead is None:
						self._polyHead = newTerm
				else:
						self._polyTail.next = newTerm
				
				self._polyTail = newTerm

	def printPoly(self):
		"""
		Extra method which is not necessary for the Polynomial ADT.Just using it to show up the result of the operations
		between two or more polynomials.
		"""
		curNode = self._polyHead
		while curNode is not None:
				if curNode.next is not None:
						print "%(coefficient)sx^%(degree)s + " % {"coefficient":curNode.coefficient, \
							"degree":curNode.degree},  #string format based on the dictionary.
				else:
						print "%(coefficient)sx^%(degree)s" % {"coefficient":curNode.coefficient, \
							"degree":curNode.degree}
						print

				curNode = curNode.next


if __name__ == "__main__":
		leftPoly = Polynomial(2, 5)
		leftPoly += Polynomial(1, 3)
		leftPoly += Polynomial(0, -10)

		rightPoly = Polynomial(3, 2)
		rightPoly += Polynomial(2, 4)
		rightPoly += Polynomial(0, 3)

		addPoly = leftPoly + rightPoly
		subPoly = leftPoly - rightPoly
		mulPoly = leftPoly * rightPoly
		evalPoly = leftPoly.evaluate(10)

		print "The addition of the two polynomials is:"
		addPoly.printPoly()


		print "The substraction of the two polynomials is:"
		subPoly.printPoly()
		
		print "The multiplication of the two polynomials is:"
		mulPoly.printPoly()

		print "The evaluation of the leftPoly is:", evalPoly

