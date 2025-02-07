import sys
sys.setrecursionlimit(10**6)

values = [0]
weights = [0]

with open("problem16_7.txt") as file:
    knapsack_capacity, total_items = map(int, file.readline().strip().split(" "))
    for line in file:
        value, weight = map(int, line.strip().split(" "))
        values.append(value)
        weights.append(weight)
        
tab = {}

def optimal(i, x):
    if i == 0 or x == 0:
        return 0
    
    key = (i,x)
    
    if key in tab:
        return tab[key]
    
    if weights[i] > x:
        result = optimal(i-1, x)
    else:
        case_1 = optimal(i-1, x)
        case_2 = optimal(i-1, x - weights[i]) + values[i]
        result = max(case_1, case_2)
    
    tab[key] = result
    return result

print(optimal(total_items, knapsack_capacity))

n = total_items
s = knapsack_capacity
optimal_items = []

while n > 0 and s > 0:
    if weights[n] <= s and tab[(n-1, s - weights[n])] + values[n] > tab[(n-1, s)]:
        optimal_items.append(n)
        s -= weights[n]
    n -= 1
    
print(optimal_items)