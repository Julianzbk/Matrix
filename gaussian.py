class InvalidMatrixError(Exception):
    pass

class Fraction:
    def __init__(self, num, denom):
        if type(num) != int or type(denom) != int:
            raise ValueError
        self.num = num
        self.denom = denom

    def __str__(self):
        return f"{self.num}/{self.denom}"

class Matrix:
    def __init__(self, rows: list[list[int]]):
        n = len(rows[0])
        for row in rows:
            if len(row) != n:
                raise InvalidMatrixError("Inconsistent number of columns")
        self.matrix = rows
        self.m = len(rows)
        self.n = n

    def swap(self, row_a, row_b):
        row_a -= 1
        row_b -= 1
        try:
            self.matrix[row_a], self.matrix[row_b] = self.matrix[row_b], self.matrix[row_a]
        except IndexError:
            raise IndexError("Invalid row numbers")

    def multiply(self, row: int, factor: int or Fraction):
        if type(factor) != int and type(factor) != Fraction:
            raise TypeError("Invalid factor")
        row -= 1
        try:
            for n in range(self.n):
                self.matrix[row][n] *= factor
        except IndexError:
            raise IndexError("Invalid row number")

    def add(self, target: int, addend: int, factor: int or Fraction):
        if type(factor) != int and type(factor) != Fraction:
            raise TypeError("Invalid factor")
        target -= 1
        addend -= 1
        try:
            for n in range(self.n):
                self.matrix[target][n] += factor * self.matrix[addend][n]
        except IndexError:
            raise IndexError("Invalid row number")

    def zero_rows(self) -> tuple:
        rows = []
        for m in range(self.m):
            if self.matrix[m] == [0] * self.n:
                rows.append(m + 1)
        return tuple(rows)

    def __str__(self):
        string = f"{self.m} x {self.n} matrix:\n"
        # padding = max([len(str(row)) for row in self.matrix]) // self.n - 3
        for m in range(self.m):
            for n in range(self.n):
                string += str(self.matrix[m][n]) + ' ' #* padding
            string += '\n'
        return string

def solve(matrix: list[list[int]] or Matrix) -> Matrix:
    if type(matrix) == Matrix:
        pass
    elif type(matrix) == list:
        matrix = Matrix(matrix)
    else:
        raise TypeError("Invalid matrix type")

    matrix.multiply(2, 2)
    matrix.add(3, 1, -1)
    return matrix


if __name__ == "__main__":
    print("Enter rows of augmented matrix as numbers seperated by one space.\n"
          "End matrix with 'q'.")
    mtx = []
    line = input()
    while line != 'q':
        mtx.append([int(n) for n in line.strip().split()])
        line = input()
    mtx = solve(mtx)
    print(mtx)