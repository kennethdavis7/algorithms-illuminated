values = [0]
weights = [0]

with open("problem16_7test.txt") as file:
    knapsack_capacity, total_items = map(int, file.readline().strip().split(" "))
    for line in file:
        value, weight = map(int, line.strip().split(" "))
        values.append(value)
        weights.append(weight)

A = [[0] * (knapsack_capacity + 1) for i in range(total_items + 1)]

for i in range(1, total_items + 1):
    for j in range(knapsack_capacity + 1):
        if weights[i] > j:
            A[i][j] = A[i-1][j]
        else:
            A[i][j] = max(A[i-1][j], A[i-1][j-weights[i]] + values[i])

print(A[total_items][knapsack_capacity])

n = total_items
s = knapsack_capacity
optimal_items = []
while n > 0 and s > 0:
    if weights[n] <= s and A[n-1][s-weights[n]] + values[n] > A[n-1][s]:
        optimal_items.append(n)
        s -= weights[n]
    n -= 1
    
print(optimal_items)




