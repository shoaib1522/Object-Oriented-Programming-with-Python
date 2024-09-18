class Matrix:
    def __init__(self, row, cols):
        self.__rows = rows
        self.__cols = cols
        self.__data = [[0 for c in range(cols)] for r in range(rows)]      

    def NullMatrix(self, row, cols):
        return Matrix(rows, cols)

    def SquareMatrix(self, size):
        return Matrix(size, size)

    def IdentityMatrix(self, size):
        tm = SquareMatrix(size)
        for j in range(size):
            tm[j][j] = 1     # somehow

    def RowMatrix(self, size):
        return Matrix(1, size)

    def ColumnMatrix(self, size):
        tm = Matrix(size, 1)

    def __str__(self):
        
    def __repr__(self):
        
    def __reduce__(self):
        
    def __eq__(self, other):   # for equal matrices
        
    def __ne__(self, other):    # for unequal matrices

    def __neg__(self):    # negative of a matrices

    # other relational/condition operations <, <=, >, >=

    #how to use following in 2D matrix
    def __getitem__(self, index):
    def __setitem__(self, index, value):
    #def __delitem__(self, index):
    
        
    @property
    def rows(self):  

    @property
    def cols(self):   

    @property
    def size(self):   

    @property
    def isRowMatrix(self):   

    @property
    def isColumnMatrix(self):   

    @staticmethod
    def additionCompatible(self, other):
    
    @staticmethod
    def multiplicationCompatible(self, other):
    
    def __add__(self, other):
    
    def __sub__(self, other):
    
    def __mul__(self, other):
    
    def __rmul__(self, other):
    
    def __add__(self, other):
    
    def transpose(self):
    
    def subMatrix(self, rs, re, cs, ce):
    
    def isSquareMatrix(self):
    
    def isNullMatrix(self):
    
    def isIdentityMatrix(self):
    
    def isRowMatrix(self):
    
    def isColumnMatrix(self):
    
    def isUpperTriMatrix(self):
    
    def isLowerTriMatrix(self):
    
    def isDefiniteMatrix(self):
    
    def isOrthogonalMatrix(self):
    
    def isEmptyMatrix(self):

    def rowAdd(self, r1, r2):
    
    def rowMul(self, r, n):
    
    def rowSwap(self, r1, r2):
    
    def colAdd(self, r1, r2):
    
    def colMul(self, r, n):
    
    def colSwap(self, r1, r2):
    
    #some more of your choice

    # in case matrix is square
    determinant
    adjoint
    trace
    inverse
    cofactor matrix
    adjugate
    some functions of matrix discussed above should be here