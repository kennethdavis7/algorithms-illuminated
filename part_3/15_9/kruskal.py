from datetime import datetime

start = datetime.now()

class UnionFind:
    def __init__(self, size):
        self.parent = {i: i for i in range(1, size + 1)}
        self.size = {j: 1 for j in range(1, size + 1)}
        
    def find(self, i):
        return self.parent[i]

    def unionBySize(self, i, j):
        parent_i = self.find(i)
        parent_j = self.find(j)
        
        if parent_i == parent_j:
            return
        
        if self.size[parent_i] < self.size[parent_j]:
            smaller, larger = parent_i, parent_j
        else:
            smaller, larger = parent_j, parent_i
        
        for i in self.parent:
            if self.parent[i] == smaller:
                self.parent[i] = larger
        
        self.size[larger] += self.size[smaller]
        

edges = []

with open("problem15_9.txt") as file:
    totalNodes, totalEdges = map(int, file.readline().strip().split(" "))
    
    for line in file:
        node, neighbor, cost = map(int, line.split(" "))
        
        edges.append((node, neighbor, cost))

def kruskal(edges):
    uf = UnionFind(totalNodes)
    T = []
    
    def func(e):
        return e[2]
    
    edges.sort(key=func)
    
    for edge in edges:
        if uf.find(edge[0]) != uf.find(edge[1]):
            T.append(edge)
            uf.unionBySize(edge[0], edge[1])
    
    return T

MSTCost = 0
for edge in kruskal(edges):
    MSTCost += edge[2]
print(MSTCost)

end = datetime.now()
td = (end - start).total_seconds() * 10**3
print(f"The time of execution of above program is : {td:.03f}ms")
