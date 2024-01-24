from fraction import *

class InvalidMatrixError(Exception):
    def __init__(self, msg="Invalid matrix"):
        super().__init__(msg)

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


class InvalidOperationError(Exception):
    def __init__(self, msg="Invalid operation"):
        super().__init__(msg)


def ero(matrix: Matrix) -> None:
    line = input("Enter matrix operation in the form of an equation:\n")
    line = line.upper().split()
    if line[1] == '=':  # R1 = R1 + 3R3
        target = get_row_number(line[0])

        if len(line) == 3:  # R1 = 2R1
            factor = get_row_number(line[2])[0]
            matrix.multiply(target, factor)
            return

        operator = line[3]

        if line[2] == line[0]:
            factor, addend = get_row_number(line[2])
            if operator == '+':
                matrix.add(target, addend, factor)
            elif operator == '-':
                matrix.add(target, addend, -factor)
            else:
                raise InvalidOperationError("Invalid operator")
        elif line[3] == line[0]:  # R1 = 3R3 + R1
            factor, addend = get_row_number(line[3])
            if operator == '+':
                matrix.add(target, addend, factor)
            elif operator == '-':
                matrix.add(target, addend, -factor)
            else:
                raise InvalidOperationError("Invalid operator")
        else:
            raise InvalidOperationError

def get_row_number(exp: str):
    """ '4R3' -> (4, 3) """
    r_loc = exp.find('R')
    if r_loc == -1:
        raise InvalidOperationError
    try:
        if r_loc == 0:
            if '/' in exp:
                Fraction()
            return int(exp[r_loc+1:])
        else:
            return int(exp[:r_loc]), int(exp[r_loc+1:])
    except ValueError:
        raise InvalidOperationError("Invalid row number")


if __name__ == "__main__":
    mtx = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    while True:
        ero(mtx)
        print(mtx)
