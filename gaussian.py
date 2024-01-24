from matrix import *

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