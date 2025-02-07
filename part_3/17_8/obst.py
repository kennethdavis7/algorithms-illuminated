with open("problem17_8optbst.txt") as file:
    n = int(file.readline().strip())
    freq = list(map(int, file.readline().strip().split(",")))
    
freq = [0] + freq

dp = [[0] * (n+1) for _ in range(n+1)]

for s in range(n):
    for i in range(1, n-s+1):
        j = i + s
        
        minimum = float('inf')
        
        pk = sum(freq[k] for k in range(i, j + 1))
        
        for r in range(i, j+1):
            left_cost = dp[i][r - 1] if r > i else 0 
            right_cost = dp[r + 1][j] if r < j else 0 
            cost = left_cost + right_cost
            minimum = min(minimum, cost)
        
        dp[i][j] = pk + minimum

print(dp[1][n])
