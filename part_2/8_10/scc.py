adjacency_list = {}
reversed_adjacency_list = {}
finishing_times = {}
current_time = [1]

def make_alist(edges):
    all_nodes = set()
    for edge in edges:
        node1, node2 = edge
        all_nodes.add(node1)
        all_nodes.add(node2)

    for node in all_nodes:
        adjacency_list[node] = []
        reversed_adjacency_list[node] = []

    for edge in edges:
        node1, node2 = edge
        adjacency_list[node1].append(node2)
        reversed_adjacency_list[node2].append(node1)

edges = []
with open("problem8_10.txt") as file:
    for line in file:
        edge1, edge2 = line.split()
        edges.append([int(edge1), int(edge2)])

make_alist(edges)

def SCC_sizes():
    visited = {node: False for node in adjacency_list}

    def dfs_reversed_iterative(node):
        stack = [(node, False)] 
        while stack:
            current, is_exiting = stack.pop()
            if is_exiting:
                finishing_times[current_time[0]] = current
                current_time[0] += 1
            elif not visited[current]:
                visited[current] = True
                stack.append((current, True))  
                for neighbor in reversed_adjacency_list[current]:
                    if not visited[neighbor]:
                        stack.append((neighbor, False))

    for node in adjacency_list.keys():
        if not visited[node]:
            dfs_reversed_iterative(node)


    visited = {node: False for node in adjacency_list}
    SCC_sizes = []

    def dfs_original_iterative(node):
        stack = [node]
        size = 0
        while stack:
            current = stack.pop()
            if not visited[current]:
                visited[current] = True
                size += 1
                for neighbor in adjacency_list[current]:
                    if not visited[neighbor]:
                        stack.append(neighbor)
        return size

    for time in range(len(finishing_times), 0, -1):
        node = finishing_times[time]
        if not visited[node]:
            size = dfs_original_iterative(node)
            SCC_sizes.append(size)
    
    return SCC_sizes


def get_top_5_SCC_sizes(SCC_sizes):
    top_5 = [0] * 5

    for size in SCC_sizes:
        if size > top_5[-1]:
            top_5[-1] = size
            top_5.sort(reverse=True)
    
    return top_5

print(get_top_5_SCC_sizes(SCC_sizes()))

# Recursive approach
# def kosaraju():
#     n = len(adjacency_list.keys())
#     visited = {node: False for node in adjacency_list}
    
#     def dfs_reversed(node):
#         visited[node] = True
#         for neighbor in reversed_adjacency_list[node]:
#             if not visited[neighbor]:
#                 dfs_reversed(neighbor)
#         finishing_times[current_time[0]] = node
#         current_time[0] += 1
    
#     for i in range(n, 0, -1):
#         if not visited[i]:
#             dfs_reversed(i)
    
#     visited = {node: False for node in adjacency_list}
#     SCC_sizes = []

#     def dfs_original(node, SCC_nodes):
#         visited[node] = True
#         for neighbor in adjacency_list[node]:
#             if not visited[neighbor]:
#                 dfs_original(neighbor, SCC_nodes)
#         SCC_nodes.append(node)
    
#     for time in range(len(finishing_times), 0, -1):
#         node = finishing_times[time]
#         if not visited[node]:
#             SCC_nodes = []
#             dfs_original(node, SCC_nodes)
#             SCC_sizes.append(len(SCC_nodes))
    
#     return SCC_sizes

