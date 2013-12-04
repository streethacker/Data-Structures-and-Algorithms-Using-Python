from array import Array

class MultiArray:
	def __init__(self, *dimension):
		assert len(dimension) > 1, "The multi array must have 2 or more dimensions."
		self._dims = dimension
		size = 1
		for d in dimension:
				assert d > 0, "Dimension must be > 0."
				size *= d

		self._elements = Array(size)
		self._factors = Array(len(self._dims))
		
		self._computeFactors()

	def numDims(self):
		return len(self._dims)

	def length(self, dim):
		assert dim > 1 and dim < len(self._dims),\
		"Dimension component out of range."
		return self._dims[dim-1]

	def clear(self, value):
		self._elements.clear(value)

	def __getitem__(self, ndxTuple):
		assert len(ndxTuple) == self.numDims(), \
		"Invalid # of array subscripts."
		index = self._computeIndex(ndxTuple)
		assert index is not None, "Array subscript out of range."
		return self._elements[index]

	def __setitem__(self, ndxTuple, value):
		assert len(ndxTuple) == self.numDims(), \
		"Invalid # of array subscripts."
		index = self._computeIndex(ndxTuple)
		assert index is not None, "Array subscript out of range."
		self._elements[index] = value

	def _computeIndex(self, idx):
		offset = 0
		for j in range(len(idx)):
				if idx[j] < 0 or idx[j] >= self._dims[j]:
						return None
				else:
						offset += idx[j] * self._factors[j]
		return offset

	def _computeFactors(self):
		max_idx = len(self._factors) - 1
		self._factors[max_idx] = 1

		for i in range(max_idx, 0, -1):
				self._factors[i-1] = self._dims[i]*self._factors[i]


if __name__ == "__main__":
		test = MultiArray(3, 3, 3)
		test.clear(10)
		test[1, 2, 1] = 55
		print test[1, 1, 1]
		print test[1, 2, 1]
