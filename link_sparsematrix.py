from array import Array

class _MatrixElementNode:
	def __init__(self, col, value):
		self.col = col
		self.value = value
		self.next = None


class SparseMatrix:
	def __init__(self, numRows, numCols):
		self._numCols = numCols
		self._listOfRows = Array(numRows)

	def numRows(self):
		return len(self._listOfRows)

	def numCols(self):
		return self._numCols

	def __setitem__(self, ndxTuple, value):
		row, col = ndxTuple[0], ndxTuple[1]
		assert row < self.numRows() and col < self.numCols(), \
			"The index is out of range."

		preNode = None
		curNode = self._listOfRows[row]

		while curNode is not None and curNode.col != col:
				preNode = curNode
				curNode = curNode.next

		if curNode is not None and curNode.col == col:
				if value == 0.0:
						if curNode == self._listOfRows[row]:
								self._listOfRows[row] = curNode.next
						else:
								preNode.next = curNode.next
				else:
						curNode.value = value
		elif value != 0.0:
				newNode = _MatrixElementNode(col, value)
				newNode.next = curNode

				if curNode == self._listOfRows[row]:
						self._listOfRows[row] = newNode
				else:
						preNode.next = newNode

	def __getitem__(self, ndxTuple):
		row, col = ndxTuple[0], ndxTuple[1]
		assert row < self.numRows() and col < self.numCols(), \
			"The index is out of range."

		curNode = self._listOfRows[row]

		while curNode is not None and curNode.col != col:
				curNode = curNode.next

		if curNode is not None and curNode.col == col:
				return curNode.value
		else:
				return 0

	def scaleBy(self, scalar):
		for row in range(self.numRows()):
				curNode = self._listOfRows[row]
				while curNode is not None:
						curNode.value *= scalar
						curNode = curNode.next

	def __add__(self, rhsMatrix):
		assert rhsMatrix.numRows() == self.numRows() and \
			rhsMatrix.numCols() == self.numCols(), \
			"Matrix sizes not compatable for adding."

		newMatrix = SparseMatrix(self.numRows(), self.numCols())

		for row in range(self.numRows()):
				curNode = self._listOfRows[row]
				while curNode is not None:
						newMatrix[row, curNode.col] = curNode.value
						curNode = curNode.next

		for row in range(rhsMatrix.numRows()):
				curNode = rhsMatrix._listOfRows[row]
				while curNode is not None:
						value = newMatrix[row, curNode.col]
						value += curNode.value
						newMatrix[row, curNode.col] = value
						curNode = curNode.next

		return newMatrix

	def __sub__(self, rhsMatrix):
		assert rhsMatrix.numRows() == self.numRows() and \
			rhsMatrix.numCols() == self.numCols(), \
			"Matrix sizes not compatable for adding."

		newMatrix = SparseMatrix(self.numRows(), self.numCols())

		for row in range(self.numRows()):
				curNode = self._listOfRows[row]
				while curNode is not None:
						newMatrix[row, curNode.col] = curNode.value
						curNode = curNode.next

		for row in range(rhsMatrix.numRows()):
				curNode = rhsMatrix._listOfRows[row]
				while curNode is not None:
						value = newMatrix[row, curNode.col]
						value -= curNode.value
						newMatrix[row, curNode.col] = value
						curNode = curNode.next

		return newMatrix

	def transpose(self):
		newMatrix = SparseMatrix(self.numCols(), self.numRows())

		for row in range(self.numRows()):
				curNode = self._listOfRows[row]
				while curNode is not None:
						newMatrix[curNode.col, row] = curNode.value
						curNode = curNode.next

		return newMatrix

	def __mul__(self, rhsMatrix):
		assert self.numCols() == rhsMatrix.numRows(), \
			"Matrix sizes not compatable for multipy."						

		newMatrix = SparseMatrix(self.numRows(), rhsMatrix.numCols())

		for r in range(self.numRows()):
				for c in range(rhsMatrix.numCols()):
						for cx in range(self.numCols()):
								newMatrix[r, c] += self[r, cx] * rhsMatrix[cx, c]

		return newMatrix


	def printMatrix(self):
		for row in range(self.numRows()):
				for col in range(self.numCols()):
						print self[row, col], "\t",
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
