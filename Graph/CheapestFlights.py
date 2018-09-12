class FlightGraph(object):
    def __init__(self):
        self.adj = {}


    def addVertex(self, fromVertex, toVertex):
        if fromVertex in self.adj:
            self.adj[fromVertex].append(toVertex)
        else :
            self.adj[fromVertex] = [toVertex]


if __name__ == '__main__':
    #Input 1
    n = 3
    edges = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src = 0
    dst = 2
    k = 1


    for edge in edges:
        