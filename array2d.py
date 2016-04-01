from array1d import Array


class Array2D:
    """
    The implementation of the Array2D abstract data type
    using an array of arrays. The constructor creates a
    data field named _theRows to which an Array object
    is assigned. This is the main array used to stores t
    -he references to the other arrays that are created
    each row in the 2-D array.
    """

    def __init__(self, numRows, numCols):
        self._theRows = Array(numRows)

        for i in range(numRows):
            self._theRows[i] = Array(numCols)

    def numRows(self):
        """
        The numRows() method can obtain the number of rows
        by checking the length of the main array, which co
        -ntains an element for each row in the 2-D array.
        """
        return len(self._theRows)

    def numCols(self):
        """
        The numCols() method can simply check the length of
        any of the 1-D arrays used to store the individual
        rows.
        """
        return len(self._theRows[0])

    def clear(self, value):
        for row in self._theRows:
            row.clear(value)

    def __getitem__(self, ndxTuple):
        """
        NOTE:
        +--------------------------------------------------------------+
        I.When a multi-component subscript is specified(i.e. y = x[i, j]),
        Python automatically stores the components in a tuple in the or
        -der listed within the brackets and passes the tuple to the ndx
        -Tuple argument of the __getitem__ method.

        II.The len() method can only be used with the collection types,
        not individual values. It does generate its own error, however,
        when used improperly. Thus len() function is used to ensure two
        components are supplied for all Array2D objects.
        +--------------------------------------------------------------+
        """
        assert len(ndxTuple) == 2, "Invalid number of array subscripts."
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self.numRows()\
            and col >= 0 and col < self.numCols, \
            "Array subscript out of range."
        return self._theRows[row][col]

    def __setitem__(self, ndxTuple, value):
        """
        NOTE:
        +---------------------------------------------------------------+
        I.ndxTuple --> the same use as the ndxTuple parameter in the
        __getitem__ method.

        II.The order of the two parameters: ndxTuple&value is extremely
        important.
        +---------------------------------------------------------------+
        """
        assert len(ndxTuple) == 2, "Invalid number of array subscripts."
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self.numRows() \
            and col >= 0 and col < self.numCols(),\
            "Array subscript out of range."
        self._theRows[row][col] = value

if __name__ == "__main__":
    arr2d = Array2D(3, 4)
    arr2d.clear(100)
    print arr2d[1, 2]
