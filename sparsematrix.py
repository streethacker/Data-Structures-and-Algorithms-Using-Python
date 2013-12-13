__author__ = "streethacker"

#/usr/bin/python
#-*- coding:utf-8 -*-

#Data Structures and Algorithms Using Python
#CHAPTER 4: Algorithm Analysis
#Listing 4.2: sparsematrix.py

class _MatrixElement:
	def __init__(self, row, col, value):
		self.row = row
		self.col = col
		self.value = value


class SparseMatrix:
	"""
	A matrix containing a large number of zero elements is called a sparse matrix.
	Sparse matrices are very common in scientific applications, especially those
	dealing with systems of linear equations.

	Here we define and implement a class for storing and working with sparse matric
	-es in which the non-zero elements are stored in a list.
	"""
	def __init__(self, numRows, numCols):
		"""
		The constructor defines three attributes for storing the data related to the
		sparse matrix:

		The _elementList field stores _MatrixElement objects representing the non-ze
		-ro elements. Instances of the storage class contain not only the value for a
		specific element but also the row and column indices indicating its location
		within the matrix. The _numRows and _numCols fields are used to store the dis
		-mensions of the matrix.
		"""

		self._numRows = numRows
		self._numCols = numCols
		self._elementList = list()

	def numRows(self):
		return self._numRows

	def numCols(self):
		return self._numCols

	def __getitem__(self, ndxTuple):
		assert ndxTuple[0] < self._numRows and ndxTuple[1] < self._numCols, \
			"Index is out of range."

		ndx = self._findPosition(ndxTuple[0], ndxTuple[1])

		if ndx is not None:
				return self._elementList[ndx].value
		else:
				return 0

	def __setitem__(self, ndxTuple, scalar):
		"""
		Modifying an element:

		1.The element is in the list(and thus non-zero) and the new value is
		  non-zero.  -->  modify the element

		2.The element is in the list, but the new value is zero, turning the
		  element into a zero element.  -->  pop the element from the list

		3.The element is not currently in the list and the new value is non-
		  zero.  -->  append the new element to the list

		4.The element is not currently in the list, and the new value is zero.
		  -->  omit(do nothing to the list)
		"""

		assert ndxTuple[0] < self._numRows and ndxTuple[1] < self._numCols, \
			"Index is out of range."

		ndx = self._findPosition(ndxTuple[0], ndxTuple[1])

		if ndx is not None:
				if scalar != 0.0:
						self._elementList[ndx].value = scalar
				else:
						self._elementList.pop(ndx)
		else:
				if scalar != 0.0:
						element = _MatrixElement(ndxTuple[0], ndxTuple[1], scalar)
						self._elementList.append(element)

	def scaleBy(self, scalar):
		for element in self._elementList:
				element.value *= scalar

	def transpose(self):
		"""
		Only need to exchange the row and column number of the non-zero element
		which is kept in the _elementList.
		"""
		newMatrix = SparseMatrix(self.numCols(), self.numRows())

		for element in self._elementList:
				dupElement = _MatrixElement(element.col, element.row, element.value)
				newMatrix._elementList.append(dupElement)

		return newMatrix

	def __add__(self, rhsMatrix):
		"""
		Matrix addition:

		1.Verify the size of the two matrices to ensure they are the same as required
		  by matrix addition.

		2.Create a new SparseMatrix object with the same number of rows and columns a
		-s the other two.

		3.Duplicate the elements of the self matrix and store them in the new matrix.

		4.Iterate over the element list of the righthand side matrix(rhsMatrix) to add
		the non-zero values to the corresponding elements in the new matrix.
		"""

		assert rhsMatrix.numRows() == self.numRows() and \
			rhsMatrix.numCols() == self.numCols(), \
			"Matrix sizes not compatible for the add operation."

		newMatrix = SparseMatrix(self.numRows(), self.numCols())

		#Duplicate the lhs matrix. The elements are mutable, thus we must create new
		#objects and not simply copy the references.
		for element in self._elementList:
				dupElement = _MatrixElement(element.row, element.col, element.value)
				newMatrix._elementList.append(dupElement)

		for element in rhsMatrix._elementList:
				value = newMatrix[element.row, element.col]
				value += element.value

				newMatrix[element.row, element.col] = value

		return newMatrix

	def __sub__(self, rhsMatrix):
		assert rhsMatrix.numRows() == self.numRows() and \
			rhsMatrix.numCols() == self.numCols(), \
			"Matrix sizes not compatible for the add operation."

		newMatrix = SparseMatrix(self.numRows(), self.numCols())

		for element in self._elementList:
				dupElement = _MatrixElement(element.row, element.col, element.value)
				newMatrix._elementList.append(dupElement)

		for element in rhsMatrix._elementList:
				value = newMatrix[element.row, element.col]
				value -= element.value

				newMatrix[element.row, element.col] = value

		return newMatrix

	def __mul__(self, rhsMatrix):
		assert self.numCols() == rhsMatrix.numRows(),\
			"Matrix sizes not compatible for the add operation."
			
		newMatrix = SparseMatrix(self.numRows(), rhsMatrix.numCols())

		for r in range(self.numRows()):
				for c in range(rhsMatrix.numCols()):
						for cx in range(self.numCols()):
								newMatrix[r, c] += self[r, cx] * rhsMatrix[cx, c]

		return newMatrix

			
	def _findPosition(self, row, col):
		"""
		The helper method _findPosition() performs a linear search by iterating
		through the element list looking for an entry with the given row and co
		-lumn indices.
		"""
		n = len(self._elementList)

		for i in range(n):
				if row == self._elementList[i].row and \
				   col == self._elementList[i].col:
				   return i

		return None

	def printMatrix(self):
		for r in range(self.numRows()):
				for c in range(self.numCols()):
						ndx = self._findPosition(r,c)
						if ndx is not None:
								print self._elementList[ndx].value, "\t",
						else:
								print 0, "\t",
				print 



if __name__ == "__main__":
		lspMtx, rspMtx = SparseMatrix(3, 4), SparseMatrix(3,4)

		newMtx = SparseMatrix(3, 4)

		transMtx = SparseMatrix(4,3)

		lspMtx[0,1] = 1
		lspMtx[1,2] = 2


		rspMtx[0,0] = 4
		rspMtx[1,2] = 1
		rspMtx[2,3] = 3

		newMtx = lspMtx + rspMtx

		print "The left Matrix contents:"
		lspMtx.printMatrix()

		print
		
		print "The right Matrix contents:"
		rspMtx.printMatrix()

		print

		print "The new Matrix contents:"
		newMtx.printMatrix()

		transMtx = newMtx.transpose()

		print

		print "The new Matrix after transpose:"
		transMtx.printMatrix()

		mul_lMtx = SparseMatrix(3,3)
		mul_rMtx = SparseMatrix(3,2)

		mul_lMtx[0,2], mul_lMtx[1,1] = 1, 1
		mul_rMtx[1,0], mul_rMtx[2,1] = 1, 1

		mul_newMtx = mul_lMtx * mul_rMtx

		print 

		print "The two matrices multipication is:"
		mul_newMtx.printMatrix()
