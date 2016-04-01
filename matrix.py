__author__ = "streethacker"

#/usr/bin/python
#-*-coding:utf-8-*-

# Data Structures and Algorithms Using Python
# CHAPTER 2: Matrix
# Listing 2.3: matrix.py

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
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                self[r, c] += scalar

    def multiplyBy(self, scalar):
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                self[r, c] *= scalar

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

    def __mod__(self, num):
        assert int(num) == num, "The value num must be an integer."
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                self[r, c] %= num

    def inverseSpecialMatrix(self):
        assert self.numRows() == self.numCols() and self.numRows() == 2 and \
            self[0, 0] * self[1, 1] - self[0, 1] * self[1, 0] != 0,\
            "This function is only designed for 2*2 matrices which meet the conditions: ab - cd != 0"

        scalar = 1 / float((self[0, 0] * self[1, 1] - self[0, 1] * self[1, 0]))

        self[0, 1] *= -1
        self[1, 0] *= -1

        self.multiplyBy(scalar)

    def printMatrix(self):
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                print self[r, c], "\t",
            print


if __name__ == "__main__":
    import sys
    MSG = len(sys.argv) >= 2 and sys.argv[
        1] or "meet me at the usual place at then rather than eight o'clock"

    DICT_OF_MAP = {
        k: v for (
            k,
            v) in enumerate(
            'abcdefghijklmnopqrstuvwxyz',
            0)}  # (integer, letter)
    REVERSE_DICT_OF_MAP = {
        v: k for (
            k,
            v) in enumerate(
            'abcdefghijklmnopqrstuvwxyz',
            0)}  # (letter, integer)

    characters = [REVERSE_DICT_OF_MAP[item]
                  for item in MSG.lower() if ord(item) >= 97 and ord(item) <= 122]

    key_mtx = Matrix(2, 2)
    key_mtx[0, 0], key_mtx[0, 1] = 9, 4
    key_mtx[1, 0], key_mtx[1, 1] = 5, 7

    code = [(characters[i], characters[i + 1])
            for i in range(len(characters) - 1) if i % 2 == 0]

    msg_mtx = Matrix(2, 1)

    rst_mtx = Matrix(2, 1)

    rst_stack = []

    ascd = 1
    for k, v in code:
        msg_mtx[0, 0], msg_mtx[1, 0] = k, v
        rst_mtx = key_mtx * msg_mtx
        rst_mtx % 26
        rst_stack.append(rst_mtx)
        print "C%s:" % ascd
        print "+----+"
        rst_mtx.printMatrix()
        print "+----+"
        print
        ascd += 1

    print "The final Encrypted message is:"
    for mtx in rst_stack:
        for r in range(mtx.numRows()):
            for c in range(mtx.numCols()):
                print DICT_OF_MAP[mtx[r, c]],

    print
    print
