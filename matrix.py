__author__ = "streethacker"

#/usr/bin/python
#-*-coding:utf-*-

#Data Structures and Algorithms Using Python
#CHAPTER 2: Matrix
#Listing 2.3: matrix.py

from array2d import Array2D

class Matrix:
	"""
	A matrix is a collection of scalar values arranged in rows
	and columns as a rectangular grid of a fixed size. The ele
	-ments of the matrix can be accessed by specifying a given
	row and column index with indices starting at 0.
	"""
	def __init__(self, numRows, numCols):
		"""
		Implementation of the Matrix ADT using a 2-D array. Cre
		-ates a matrix of size numRows*numCols initialized to 0.
		"""
		self._theGrid = Array2D(numRows, numCols)
		self._theGrid.clear(0)

	def numRows(self):
		return self._theGrid.numRows()

	def numCols(self):
		return self._theGrid.numCols()

	def __getitem__(self, ndxTuple):
		return self._theGrid[ndxTuple[0], ndxTuple[1]]

	def __setitem__(self, ndxTuple, scalar):
		self._theGrid[ndxTuple[0], ndxTuple[1]] = scalar
		
	def scaleBy(self, scalar):
		"""
		A matrix can be uniformly scaled, which modifies each ele
		-ments of the matrix by the same scale factor. A scale 
		factor less than 1 has the effect of reducing the value of
		each element, whereas a scale factor greater than 1 increa
		-se the value of each element.
		"""
		for r in range(self.numRows):
				for c in range(self.numCols):
						self[r, c] += scalar
						
						
	def transpose(self):
		"""
		Given a m*n matrix, a transpose swaps the rows and columns
		to create a new matrix of size n*m.
		"""
		newMatrix = Matrix(self.numCols(), self.numRows())

		for r in range(self.numRows()):
				for c in range(self.numCols()):
						newMatrix[c, r] = self[r, c]

		return newMatrix
		
	def __add__(self, rhsMatrix):
		"""
		The addition operation between two matrices requires the number
		of rows in the matrix on the lefthand side equals t the number 
		of rows in the matrix on the righthand side, as well as, the num
		-ber of columns in the matrix on the lefthand side equal to the 
		number of columns in the matrix on the righthand side.
		"""
		assert rhsMatrix.numRows() == self.numRows() and \
			rhsMatrix.numCols() == self.numCols(), \
			"Matrix sizes not compatible for the add operation."
			
		newMatrix = Matrix(self.numRows(), self.numCols())
		
		for r in range(self.numRows()):
				for c in range(self.numCols()):
						newMatrix[r, c] = self[r, c] + rhsMatrix[r, c]
		return newMatrix
		
	def __sub__(self, rhsMatrix):
		"""
		The minus operation between two matrices need the same requisition
		as the addition operation which has been talked in the __add__() 
		method.
		"""
		assert rhsMatrix.numRows() == self.numRows() and \
			rhsMatrix.numCols() == self.numCols(), \
			"Matrix sizes not compatible for the add operation."
			
		newMatrix = Matrix(self.numRows(), self.numCols())
		
		for r in range(self.numRows()):
				for c in range(self.numCols()):
						newMatrix[r, c] = self[r, c] - rhsMatrix[r, c]
						
		return newMatrix
		
	def __mul__(self, rhsMatrix):
		"""
		This gonna to be the most complicated operation on Matrix
		ADT.

		+-----------------------------------------------------------+
		Matrix multiplication is only defined for matrices where the
		number of columns in the matrix on the lefthand side is equal 
		to the number of rows in the matrix on the righthand side.The
		result is a new matrix that contains the same number of rows
		as the matrix on the lefthand side and the same number of col
		-umns as the matrix on the righthand side.

		The mainidea of the algorithm to solve the multiplication is 
		as follows:

		for r in lefthand.Rows:
				for c in righthand.Cols:
						for x{i} in lefthand.Cols:

		then

		C{r, c} = A{r, x{0}} * B{x{0}, c} + A{r, x{1}} * B{x{1}, c}
				+ ... + A{r, x{i}} * B{x{i}, c} + ... + A{r, x{n}} 
				* B{x{n}, c}
		+-----------------------------------------------------------+
		"""
		assert self.numCols() == rhsMatrix.numRows(),\
			"Matrix sizes not compatible for the add operation."
			
		newMatrix = Matrix(self.numRows(), rhsMatrix.numCols())

		for r in range(self.numRows()):
				for c in range(rhsMatrix.numCols()):
						for cx in range(self.numCols()):
								newMatrix[r, c] += self[r, cx] * rhsMatrix[cx, c]

		return newMatrix

	def printMatrix(self):
		for r in range(self.numRows()):
				for c in range(self.numCols()):
						print self[r, c], "\t",
				print


if __name__ == "__main__":
		mtx_a = Matrix(3, 2)
		mtx_b = Matrix(2, 3)

		mtx_a[0, 0] = 0
		mtx_a[0, 1] = 1
		mtx_a[1, 0] = 2
		mtx_a[1, 1] = 3
		mtx_a[2, 0] = 4
		mtx_a[2, 1] = 5

		mtx_b[0, 0] = 6
		mtx_b[0, 1] = 7
		mtx_b[0, 2] = 8
		mtx_b[1, 0] = 9
		mtx_b[1, 1] = 1
		mtx_b[1, 2] = 0

		mtx_res = mtx_a * mtx_b

		print "The result Matrix is:"
		mtx_res.printMatrix()
