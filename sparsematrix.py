class _MatrixElement:
	def __init__(self, row, col, value):
		self.row = row
		self.col = col
		self.value = value


class SparseMatrix:
	def __init__(self, numRows, numCols):
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

	def __add__(self, rhsMatrix):
		assert rhsMatrix.numRows() == self.numRows() and \
			rhsMatrix.numCols() == self.numCols(), \
			"Matrix sizes not compatible for the add operation."

		newMatrix = SparseMatrix(self.numRows(), self.numCols())

		for element in self._elementList:
				dupElement = _MatrixElement(element.row, element.col, element.value)
				newMatrix._elementList.append(dupElement)

		for element in rhsMatrix._elementList:
				value = newMatrix[element.row, element.col]
				value += element.value

				newMatrix[element.row, element.col] = value

		return newMatrix

	def _findPosition(self, row, col):
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



