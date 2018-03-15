import math
from math import sqrt
import numbers


def zeroes(height, width):
    """
    Creates a matrix of zeroes.
    """
    g = [[0.0 for _ in range(width)] for __ in range(height)]
    return Matrix(g)


def identity(n):
    """
    Creates a n x n identity matrix.
    """
    I = zeroes(n, n)
    for i in range(n):
        I.g[i][i] = 1.0
    return I


class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################

    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise (
            ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise (NotImplementedError,
                   "Calculating determinant not implemented for matrices largerer than 2x2.")

        # TODO - your code here
        if self.h ==1:  # Calculates the determinant of a 1x1 matrix
            return self.g[0][0]
        if self.h == 2:  #Calculates the determinant of a 2x2 matrix
            return (self.g[0][0] * self.g[1][1] - self.g[0][1] * self.g[1][0])


    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise (
            ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        sum = 0
        for i in range(self.h):
            sum += self[i][i]

        return sum


    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise (ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise (NotImplementedError,
                   "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        mD = self.determinant()
        if self.h == 1:  # Calculates the inverse of a 1x1 Matrix.
            if self.g[0][0] == 0:
                raise (NotImplementedError, "The 1x1 Matrix contains 0 can't inverse")
            else:
                return [[1 / self.g[0][0]]]
        for i in range(self.h):   # Calculates the inverse of a 2x2 Matrix.
            my_Matrix = zeroes(2,2)
            my_Matrix.g[1][1] = self.g[0][0] / mD
            my_Matrix.g[0][0] = self.g[1][1] / mD
            my_Matrix.g[0][1] = - self.g[0][1] / mD
            my_Matrix.g[1][0] = - self.g[1][0] / mD
            return my_Matrix

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        t = zeroes(self.h, self.w)
        for i in range(self.h):
            for j in range(self.w):
                t[i][j] = self[j][i]
        return t

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self, idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self, other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise (ValueError,
                   "Matrices can only be added if the dimensions are the same")
            #
        # TODO - your code here
        #
        my_add = zeroes(self.h, self.w)
        for i in range(self.h):
            for j in range(self.w):
                my_add.g[i][j] = self.g[i][j] + other.g[i][j]

        return my_add

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #
        # TODO - your code here
        #
        my_neg = zeroes(self.h, self.w)
        for i in range(self.h):
            for j in range(self.w):
                my_neg.g[i][j] = - self.g[i][j]
        return my_neg


    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #
        # TODO - your code here
        #
        my_sub = zeroes(self.h, self.w)
        for i in range(self.h):
            for j in range(self.w):
                my_sub.g[i][j] = self.g[i][j] - other.g[i][j]

        return my_sub

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #
        # TODO - your code here
        #
        height = 0
        width = 0
        if isinstance(other, list):
            height = len(other)
            width = len(other[0])

        else:
            height = other.h
            width = other.w

        my_mul = zeroes(self.h, width)
        if self.w == height:
            for i in range(self.h):
                for j in range(width):
                    my_sum = 0.
                    for k in range(height):
                        if isinstance(other, list):
                            my_sum += self.g[i][k] * other[k][j]
                        else:
                            my_sum += self.g[i][k] * other.g[k][j]
                    my_mul[i][j] = my_sum
            return my_mul
        else:
            return NotImplementedError

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
            #
            # TODO - your code here
            #
        my_rmul = zeroes(self.h, self.w)
        for i in range(self.h):
            for j in range(self.w):
                my_rmul.g[i][j] = other * self.g[i][j]

        return my_rmul


