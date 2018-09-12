class TopologicalSort(object):
    def __init__(self):
        self.adj = {}


    def addEdge(self, fromEdge, toEdge):
        if fromEdge in self.adj:
            self.adj[fromEdge].append(toEdge)
        else :
            self.adj[fromEdge] =[toEdge]


    def printList(self):
        for i in self.adj:
            print (i, '-->', '->'.join([str(j) for j in self.adj[i]]))

    def topologicalSort(self, i ):
        visitedset = {}
        mystk = []
        for i in self.adj :
            if i not in visitedset :
                visitedset.add(i)

    def topo_sort_util(self, v, mystk):
        if self.adj[v]

if __name__ == '__main__':

    g = TopologicalSort()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    g.printList()
    g.topologicalSort(0)
