graph = {}

with open("problem18_8test1.txt") as file:
    n, m = map(int, file.readline().strip().split(" "))
    for line in file:
        node, neighbor, length = map(int, line.strip().split(" "))
        if node not in graph:
            graph[node] = []
        graph[node].append((neighbor, length))

def find_edge(v, w):
    for neighbor, length in graph[v]:
        if neighbor == w:
            return (v, w, length)
    
    return False

A = [[[0 for _ in range(n+1)] for _ in range(n+1)] for _ in range(n+1)]

for v in range(1, n + 1):
    for w in range(1, n + 1):
        edge = find_edge(v,w)
        if v == w:
            A[0][v][w] = 0
        elif edge != False:
            A[0][v][w] = edge[2]
        else:
            A[0][v][w] = float('inf')
            

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            A[k][i][j] = min(
                A[k - 1][i][j],
                A[k - 1][i][k] + A[k - 1][k][j]
            )

for x in range(1, n + 1):
    if A[n][x][x] < 0:
        is_negative_cycle = True
        break;
    is_negative_cycle = False

if is_negative_cycle:
    print("The graph contains negative cycle.")
else:
    shortest_shortest_dist = float('inf')
    for g in range(1, n + 1):
        for h in range(1, n + 1):
            if shortest_shortest_dist > A[n][g][h]:
                shortest_shortest_dist = A[n][g][h]
    print(shortest_shortest_dist)






