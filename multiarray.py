from array import Array

class MultiArray:
	"""
	A multi-dimensional array consists of a collection of elements
    organized into multiple dimensions. Individual elements are re
	-ferenced by specifying an n-tuple or a subscript of multiple
	components, (i_1, i_2, ... , i_n), one for each dimension of th
	-e array.

	In most programming languages, a multi-dimensional array is ac
	-tually created and stored in memory as a one-dimension array.
	With this organization, a multi-dimensional array is simply 
	an abstract view of a physical one-dimensional data structure.

	The elements can be stored in row-major order or column-major
	order, and in this MultiArray ADT, we use the row-major order
	storagement.

	"""

	def __init__(self, *dimension):
		"""
		Creates a multi-dimensional array of elements organized into
		n-dimensions with each element initially set to None. The nu
		-mber of dimensions, which is specified by the number of arg
		-uments, must be greater than 1. The individual arguments, a
		-ll of which must be greater than zero, indicate the lengths
		of the corresponding array dimensions. The dimensions are sp
		-ecified from highest to lowest, where d_1 is the highest po
		-ssible dimension and d_n is the lowest.
		"""
		assert len(dimension) > 1, "The multi array must have 2 or more dimensions."
		self._dims = dimension	#The variable argument tuple contains the dim sizes.
		size = 1	#Reference to the total number of elements in the array.
		for d in dimension:
				assert d > 0, "Dimension must be > 0."
				size *= d
		
		#The 1-D array, which is actually created in the physical memory to
		#store the multi-dimensional array in row-major order.
		self._elements = Array(size)

		#The 1-D array that stores the factors which would be used to compute
		#the offset for each element.
		self._factors = Array(len(self._dims))
		
		self._computeFactors()	#The _computeFactors() is a helper method to calculate the factors.

	def numDims(self):
		"""
		Returns the number of dimensions in the multi-dimensional array.
		"""
		return len(self._dims)

	def length(self, dim):
		"""
		Returns the length of the given array dimension. The individual
		dimensions are numbered starting from 1, where 1 represents the
		first, or highest, dimension possible in the array. Thus in an a
		-rray of three dimensions, 1 indicates the number of tables in t
		-he box, 2 is the number of rows, and 3 is number of columns.
		"""
		assert dim > 1 and dim < len(self._dims),\
		"Dimension component out of range."
		return self._dims[dim-1]

	def clear(self, value):
		self._elements.clear(value)

	def __getitem__(self, ndxTuple):
		"""
		Returns the value stored in the array at the element position
		indicated by the n-tuple(i_1, i_2, ..., i_n). All of the spec
		-ified indices must be given and they must be within the valid
		range of the corresponding array dimensions. Accessed using th
		-e element operator: y = x[1, 2].
		"""
		assert len(ndxTuple) == self.numDims(), \
		"Invalid # of array subscripts."
		index = self._computeIndex(ndxTuple)
		assert index is not None, "Array subscript out of range."
		return self._elements[index]

	def __setitem__(self, ndxTuple, value):
		"""
		Modifies the contents of the specified array element to contain
		the given value. The element if specified by the n-tuple (i_1,
		i_2, ..., i_n). All of the subscript components must be given a
		-nd they must be within the valid range of the corresponding ar
		-ray dimensions. Accessed using the lement operator: x[1, 2] = y.
		"""
		assert len(ndxTuple) == self.numDims(), \
		"Invalid # of array subscripts."
		
		#The _computeIndex() is a helper method which defined protected and used to
		#calculate the offset of each element given by position (i_1, i_2,...,i_n).
		index = self._computeIndex(ndxTuple)

		assert index is not None, "Array subscript out of range."
		self._elements[index] = value

	def _computeIndex(self, idx):
		"""
		The _computIndex() is a helper method defined to compute the offset of 
		each element given by position (i_1, i_2, ..., i_n).

		The parameter idx which receives a tuple, and then used to check the 
		index given as each dimension, if idx[j] (represents the index of jth
		dimension) small than 0 or greater than the length of jth dimension, 
		the function returns None, representing out of range. Otherwise, com
		-pute the offset using the equation: 

		+--------------------------------------------------------------------+
			index(i_1, i_2, i_3,...,i_n) = i_1 * f_1 + i_2 * f_2 
											i_n-1 * f_n-1 + i_n * 1
		+--------------------------------------------------------------------+
											
		"""
		offset = 0
		for j in range(len(idx)):
				if idx[j] < 0 or idx[j] >= self._dims[j]:
						return None
				else:
						offset += idx[j] * self._factors[j]
		return offset

	def _computeFactors(self):
		"""
		This is the second helper method defined to compute the factores before
		excute the _computeIndex() method(actually it's excuted in __init__ met
		-hod at the head of the ADT). 

		Since the size of a multi-dimensional array is fixed at the time it's cr
		-eated and cannot change during execution, the factors(represented as f_1,
		f_2,..., f_i,...,f_n above) will not change either. This can be used to 
		our advantage to reduce the number of multiplications required to compute 
		the element offsets:
			Instead of computing the factors every time an element is accessed, we
			can compute and store the factors and simply plug them into the equati
			-on when needed.

		Here is another trick, since the equation to compute the factors as follo
		-ws:
		+-------------------------------------------------------------------------+
			f_n = 1 and f_j = d_j+1 * d_j+2 * ... * d_n-1 * d_n
		+-------------------------------------------------------------------------+
		
		which can be turned into the forms as follows:

		+-------------------------------------------------------------------------+
			f_n = 1 and f_j = d_j+1 * f_j+1
		+-------------------------------------------------------------------------+

		much like a fibonacci equation, so that we can first calculate the f_n and 
		cache it, then use the result of f_n to calculate the f_n-1,then f_n-2...
		so on. Everytime we compute the ith factor, the (i+1)th is already known.In
		addition, the sequence of d is given at the moment of initializing, d_1,d_2
		...,d_i to d_n is also already known.

		It's much efficient than using the first equation.


		"""
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
