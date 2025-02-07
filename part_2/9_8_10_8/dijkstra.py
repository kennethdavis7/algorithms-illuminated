adjacencyList = {}

# with open("problem9_8test.txt") as file:
#     for line in file:
#         splitLine = line.split()
#         node = int(splitLine[0])
#         adjacencyList[node] = []
#         for i in range(1, len(splitLine)):
#             neighbor, weight = map(int, splitLine[i].split(','))
#             adjacencyList[node].append((neighbor, weight))

with open("problem9_8.txt") as file:
    for line in file:
        splitLine = line.split()
        node = int(splitLine[0])
        if node not in adjacencyList:
            adjacencyList[node] = []
        for i in range(1, len(splitLine)):
            neighbor, weight = map(int, splitLine[i].split(','))
            adjacencyList[node].append((neighbor, weight))
            if neighbor not in adjacencyList:
                adjacencyList[neighbor] = []
            adjacencyList[neighbor].append((node, weight))

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

def speedDijkstra(graph, start):
    X = set()
    H = Heap()

    key = {node: float('inf') for node in graph}
    key[start] = 0

    for node in graph:
        H.insert(key[node], node) 

    while len(X) < len(graph):
        currentKey, wStar = H.extractMin()
        
        if wStar in X:
            continue
        
        X.add(wStar)
        
        if H.length() <= 0:
            break
        

        for neighbor, weight in graph.get(wStar, []):
            if neighbor not in X:
                H.delete(neighbor)
                key[neighbor] = min(key[neighbor], currentKey + weight)
                H.insert(key[neighbor], neighbor)

    return key

startNode = 1
result = speedDijkstra(adjacencyList, startNode)

# print(result)

targets = [7,37,59,82,99,115,133,165,188,197]

print("Shortest distances from node", startNode)
for target in targets:
    print(f"Node {target}: {result[target]}")


        
# def bubbleDown(self, key, value, pos):
#     firstChild = 2 * pos + 1
#     secondChild = 2 * pos + 2
#     firstChildKey = self.heap[firstChild][0] if firstChild < len(self.heap) else float("inf")
#     secondChildKey = self.heap[secondChild][0] if secondChild < len(self.heap) else float("inf")
    
#     while firstChildKey < key or secondChildKey < key:
#         if firstChildKey <= secondChildKey:
#             firstChildValue = self.heap[firstChild][1]
#             self.heap[firstChild], self.heap[pos] = self.heap[pos], self.heap[firstChild]
#             self.position[value] = firstChild
#             self.position[firstChildValue] = pos
#         else:
#             secondChildValue = self.heap[secondChild][1]
#             self.heap[secondChild], self.heap[pos] = self.heap[pos], self.heap[secondChild]
#             self.position[value] = secondChild
#             self.position[secondChildValue] = pos
#         pos = self.position[value]
#         firstChild = 2 * self.position[value] + 1
#         secondChild = 2 * self.position[value] + 2
#         firstChildKey = self.heap[firstChild][0] if firstChild < len(self.heap) else float("inf")
#         secondChildKey = self.heap[secondChild][0] if secondChild < len(self.heap) else float("inf")
