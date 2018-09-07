class SurroundedRegions(object):
    def __init__(self, mat):
        self.mat = mat
        self.ROW = len(mat[0])
        self.COL = len(mat)
        self.flips = []
        #self.visited = [[False * self.Col] * self.ROW]
        self.visited = [[False for j in range(self.COL)] for i in range(self.ROW)]

    def isSafe(self, i, j):
        if i>=0 and j>=0 and not self.visited[i][j] and not self.mat[i][j] and not self.isBoundaryBox(i,j) :
            return True
        return False

    def isBoundaryBox(self, i, j ):
        if i==self.ROW-1 or j == self.COL-1:
            return True
        return False

    def dfs_util(self, i, j):
        x = [0, -1, 0, 1]
        y = [1, 0, -1, 0]
        for x,y in zip(x,y) :
            if self.isSafe(i+x, j+y):
                self.visited[i+x][j+y] = True
                self.flips.append([i+x, j+y])
                self.dfs_util(i+x, j+y)
                return True
        return False

    def surrounded_regions(self):
        for i in  range(self.ROW):
            for j in range(self.COL):
                if self.isSafe(i,j):
                    self.flips.append([i,j])
                    self.visited[i][j] = True
        print("->".join([str(i)+str(j) for i,j in self.flips]))


if __name__ == "__main__" :
    mat = [[1,1,1,1],[1,0,0,1],[1,1,0,1],[1,0,1,1]]
    s = SurroundedRegions(mat);
    s.surrounded_regions()
