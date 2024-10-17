# Realizado por Angie Solís y Emilia Víquez

from rayTracer.tuples import Tuples

# from tuples import Tuples

class Matrix:
    EPSILON = 0.00001
    def __init__(self, row, col):
        self.rows = row
        self.columns = col
        self.mat = []
        for r in range(0, row):
            self.mat.append([])
            for c in range(0, col):
              self.mat[r].append(0.0)
                
    def set_item(self, row, col, value):
        if 0 <= row and row < self.rows and 0 <= col and col < self.columns:
            self.mat[row][col] = value
        else:
            raise ValueError("Invalid row or column")

    def get_item(self, row, col):
        if (0 <= row < self.rows and 0 <= col < self.columns) == False:
            raise ValueError("Invalid row or column")
        return self.mat[row][col]

    def __mul__(self, other):
        if isinstance(other, Tuples):
            if self.rows == 4 and self.columns == 4:
                result = Tuples(0,0,0,0)
                tup = [other.x, other.y, other.z, other.w]
                for r in range(0, self.rows):
                    sum = 0
                    for k in range(0, 4): # since self.columns == other.rows, we don't need another variable
                        sum += self.mat[r][k] * tup[k]
                    if r == 0:
                        result.x = sum
                    elif r == 1:
                        result.y = sum
                    elif r == 2:
                        result.z = sum
                    else:
                        result.w = sum
                return result
            else:
                raise ValueError("Matrix rows and columns must be equal to 4")
        else:
            if (self.columns == other.rows): 
                result = Matrix(self.rows, other.columns)
                for row in range(0, self.rows):
                    for col in range(other.columns):
                        sum = 0
                        for k in range(0, self.columns): # since self.columns == other.rows, we don't need another variable
                            sum += self.mat[row][k] * other.mat[k][col]
                        result.mat[row][col] = sum
                return result
            else:
                raise ValueError("First matrix's rows must be equal to second's columns")

    def __add__(self, other):
        if (self.columns == other.columns and self.rows == other.rows): 
            result = Matrix(self.rows, other.columns)
            for row in range(self.rows):
                for col in range(other.columns):
                    result.mat[row][col] = self.mat[row][col] + other.mat[row][col]
            return result
        else:
          raise ValueError("First matrix's rows must be equal to second's columns")

    def __sub__(self, other):
        if (self.columns == other.columns and self.rows == other.rows): 
            result = Matrix(self.rows, other.columns)
            for row in range(self.rows):
                for col in range(other.columns):
                    result.mat[row][col] = self.mat[row][col] - other.mat[row][col]
            return result
        else:
          raise ValueError("First matrix's rows must be equal to second's columns")

    def transposing(self):
        result = Matrix(self.rows, self.columns)
        for row in range(0, self.rows):
            for col in range(0, self.columns):
                result.mat[row][col] = self.mat[col][row]
        return result

    def submatrix (self, row_del, col_del):
        result = Matrix(self.rows-1, self.columns-1)
        result_row = 0
        result_col = 0
        for row in range(0, self.rows):
            if row != row_del:
                result_col = 0
                for col in range(0, self.columns):
                    if col != col_del:
                        result.mat[result_row][result_col] = self.mat[row][col]
                        result_col = result_col + 1
                result_row = result_row + 1
        return result

    def determinant(self):
        if self.rows == 1 and self.columns == 1:
            return self.mat[0][0]
        else:
            if self.rows == 2 and self.columns == 2:
                 return self.mat[0][0]*self.mat[1][1] - self.mat[0][1]*self.mat[1][0]
            else: 
                det = 0
                for i in range(0, self.columns):
                    det = det + self.cofactor(0, i)*self.mat[0][i] 
                return det

    def minor(self, row, column):
        sub = self.submatrix(row, column)
        return sub.determinant()

    def cofactor(self, row, column):
        sub = self.submatrix(row, column)
        if (row + column) % 2 == 0:
            return sub.determinant()
        else:
            return -1*sub.determinant()

    def isInvertible(self):
        det = self.determinant()
        if det != 0:
            return True
        else:
            return False

    def inverse(self):
        result = Matrix(self.rows, self.columns)
        det = self.determinant()
        if det != 0:  # is invertible
            for r in range(0, self.rows):
                for c in range(0, self.columns):
                    result.mat[c][r] = self.cofactor(r, c) / det
        return result

    def equal(self, number1, number2):
        return abs(number1-number2) < self.EPSILON

    def __eq__(self, other):
        equal = True
        if self.columns == other.columns and self.rows == other.rows:
            for r in range(0, self.rows):
                for c in range(0, self.columns):
                    if self.equal(self.mat[r][c], other.mat[r][c]) == False:
                        equal = False
                        break
                if equal == False:
                    break
        else:
            equal = False
        return equal

    def identity(self):
        iden = Matrix(self.rows, self.columns)
        for r in range(0, self.rows):
            for c in range(0, self.columns):
                if r == c:
                    iden.mat[r][c] = 1.0
        return iden
    
    def clear(self):
        for r in range(0, self.rows):
            for c in range(0, self.columns):
                self.mat[r][c] = 0.0

    def __str__(self):
        return str(self.mat)


