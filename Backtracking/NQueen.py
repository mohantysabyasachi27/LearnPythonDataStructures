# {0, 1, 0, 0}
# {0, 0, 0, 1}
# {1, 0, 0, 0}
# {0, 0, 1, 0}


class NQueen(object):
    def __init__(self, n):
        self.sol = [[0] * n] * n
        self.N = n

    def printBoard(self):

        print("@@@@@@@@@@@@@@@@@@")
        for i in range(self.N):
            for j in range(self.N):
                print(self.sol[i][j], end=" ")
            print()
        print("@@@@@@@@@@@@@@@@@@")

    def solveNQueen(self):
        if not self.solveNQueenRec(0):
            print("Cannot be solved")
        self.printBoard()
        return True

    def solveNQueenRec(self, j):
        if j > self.N:
            return True

        for p in range(self.N):
            if self.isSafe(j, p):
                self.sol[j][p] = 1
                self.printBoard()
                if self.solveNQueenRec(j + 1) :
                    return True

            self.sol[j][p] = 0

    def isSafe(self, row, col):
        if row >= self.N & col >= self.N:
            return False

        for k in range(self.N):
            if self.sol[k][col] == 1:
                return False

        for k in range(self.N):
            if self.sol[row][k] == 1:
                return False

        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.sol[i][j] == 1:
                return False

        for i, j in zip(range(row, self.N, 1), range(col, -1, -1)):
            if self.sol[i][j] == 1:
                return False

        return True

if __name__ == "__main__":
    ob = NQueen(4)
    ob.printBoard()

    ob.solveNQueen()
