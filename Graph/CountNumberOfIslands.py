class Count_Islands(object) :
    def __init__(self, mat):
        self.mat=mat
        self.ROW = len(mat)
        self.COL = len(mat[0])
        #self.visited = [[False * self.COL] * self.ROW]
        self.visited = [[False for j in range(self.COL)] for i in range(self.ROW)]

    def printVisitedMat(self):
        print("@@@@@@@@@@@@@@@@@")
        for i in range(self.ROW):
            for j in range(self.COL):
                print(self.visited[i][j], end=" ")
            print("\n")



    def countIslands_Rec(self, pi,pj):
        if pi >=4 | pj >= 7 :
            return False
        count =0
        x = [-1,1,0,0]
        y = [0,0,-1,1]
        for i,j in zip(x,y):
            if self.isSafe(i+pi, j+pj):
                    self.visited[i+pi][j+pj] = True
                    if self.countIslands_Rec(i+pi, j+pj):
                        return True
        return False

    def isSafe(self, i, j):
        if i >= 0 and j >= 0 and i<self.ROW and j<self.COL and not self.visited[i][j] and self.mat[i][j] :
            return True
        return False

    def countIslands(self):
         i,j,count = 0,0,0
         for i in range(self.ROW):
             for j in range(self.COL):
                 if self.isSafe(i,j):
                     self.visited[i][j] = True
                     self.countIslands_Rec(i,j)
                     self.printVisitedMat()
                     count += 1
         print("count of islands", count)

if __name__ == "__main__":
    mat =  [[1,1,0,0,0,0,0],[1,1,0,0,1,1,0],[0,0,0,0,1,1,0],[0,0,1,1,0,0,0]]
    g = Count_Islands(mat)
    g.countIslands()


