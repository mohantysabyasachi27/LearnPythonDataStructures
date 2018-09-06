import math
class Sudoku_Solver(object):
    def __init__(self, matrix):
        self.matrix = matrix

    def used_in_row(self, i, size, number):
        for k in size:
            if (matrix[i][k] == number):
                return True
        return False

    def used_in_col(self , j, size, number):
        for k in size:
            if (matrix[k][j] == number):
                return True
        return False

    def used_in_box(self, i_start_box, j_start_box, size, number):
        for k1 in size:
            for k2 in size:
                if matrix[i_start_box+k1][j_start_box+k2] == number:
                    return True
        return False

    def isSafe(self, matrix, i, j, size, number):
        return not self.used_in_row(i, size, number) and not self.used_in_col(j, size, number) and not self.used_in_box(i - i%size, j - j%size , math.sqrt(size), number)


    def find_empty_box(arr, l, size):
        for row in range(size):
            for col in range(size):
                if (arr[row][col] == -1):
                    l[0] = row
                    l[1] = col
                    return True
        return False


    def solveSudoku(self, size, matrix):
        l = [0,0]
        if self.find_empty_box(matrix, l , size):
            return True

        row = l[0]
        col = l[0]
        for i in range(1, size):
            if self.isSafe(matrix, row, col, size, i):
                matrix[row][col] = i
                if(self.solveSudoku(size, matrix)):
                    return True
                matrix[row][col] = -1

        return False

if __name__ == '__main__':
    matrix = [[-1, -1, -1, 4],[-1, 2, 1, -1], [-1, 3, 4, -1],[2, -1, -1, -1]]
    s = Sudoku_Solver(matrix)
    s.solveSudoku(4, matrix)