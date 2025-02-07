from datetime import datetime

start = datetime.now()

class Heap:
    def __init__(self):
        self.heap = []
        self.position = {}
        
    def length(self):
        return len(self.heap)
    
    def bubbleUp(self, key, value, pos):
        parentPos = (pos - 1) // 2
        while pos > 0 and self.heap[parentPos][0] > key:
            parentValue = self.heap[parentPos][1]
            self.heap[parentPos], self.heap[pos] = self.heap[pos], self.heap[parentPos]
            self.position[parentValue] = pos
            self.position[value] = parentPos
            pos = parentPos
            parentPos = (self.position[value] - 1) // 2
    
    def bubbleDown(self, key, value, pos):
        while True:
            firstChild = 2 * pos + 1
            secondChild = 2 * pos + 2
            firstChildKey = self.heap[firstChild][0] if firstChild < len(self.heap) else float("inf")
            secondChildKey = self.heap[secondChild][0] if secondChild < len(self.heap) else float("inf")
            
            if firstChildKey >= key and secondChildKey >= key:
                break

            if firstChildKey <= secondChildKey:
                firstChildValue = self.heap[firstChild][1]
                self.heap[pos], self.heap[firstChild] = self.heap[firstChild], self.heap[pos]
                self.position[value] = firstChild
                self.position[firstChildValue] = pos
            else:
                secondChildValue = self.heap[secondChild][1]
                self.heap[pos], self.heap[secondChild] = self.heap[secondChild], self.heap[pos]
                self.position[value] = secondChild
                self.position[secondChildValue] = pos
                
            pos = self.position[value]
    
    def insert(self, key, value):
        entry = (key, value)
        self.heap.append(entry)
        self.position[value] = len(self.heap) - 1
        self.bubbleUp(key, value , self.position[value])
        
    def extractMin(self):
        firstEntry = self.heap[0]
        lastEntry = self.heap.pop()
        self.position.pop(firstEntry[1])
        if len(self.heap) > 0:
            self.heap[0] = lastEntry
            self.position[lastEntry[1]] = 0
            self.bubbleDown(lastEntry[0], lastEntry[1], self.position[lastEntry[1]])
        return firstEntry
    
    def delete(self, value):
        deleteEntry = self.heap[self.position[value]]
        self.heap[self.position[value]] = self.heap[len(self.heap) - 1]
        lastEntry = self.heap.pop()
        deletePosition = self.position.pop(value)
        if deletePosition != len(self.heap):
            self.position[lastEntry[1]] = deletePosition
            self.bubbleUp(lastEntry[0], lastEntry[1], self.position[lastEntry[1]])
            self.bubbleDown(lastEntry[0], lastEntry[1], self.position[lastEntry[1]])
            

graph = {}

with open("problem15_9.txt") as file:
    totalNodes, totalEdges = map(int, file.readline().strip().split(" "))
    
    for line in file:
        node, neighbor, cost = map(int, line.split(" "))
        
        if node not in graph:
            graph[node] = []
        
        if neighbor not in graph:
            graph[neighbor] = []
        
        graph[node].append((neighbor, cost))
        graph[neighbor].append((node, cost))

def prim(graph):
    s = list(graph.keys())[0]
    X = [s]
    H = Heap()
    T = []
    
    key = {}
    winner = {}
    
    for node in graph:
        if node != s:
            key[node] = float('inf')
            winner[node] = None
    
    for neighbor, cost in graph[s]:
        key[neighbor] = cost
        winner[neighbor] = (s, neighbor, cost)
    
    for node in graph:
        if node != s:
            H.insert(key[node], node)
    
    while len(X) != totalNodes:
        _, node = H.extractMin()
        
        X.append(node)
        T.append(winner[node])
        
        for neighbor, cost in graph[node]:
            if neighbor not in X:
                if cost < key[neighbor]:
                    H.delete(neighbor)
                    key[neighbor] = cost
                    winner[neighbor] = (node, neighbor, cost)
                    H.insert(cost, neighbor)
        
    return [X, T]

MSTCost = 0
for edge in prim(graph)[1]:
    MSTCost += edge[2]
print(MSTCost)

end = datetime.now()
td = (end - start).total_seconds() * 10**3
print(f"The time of execution of above program is : {td:.03f}ms")

