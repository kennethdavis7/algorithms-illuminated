with open("problem17_8sa.txt") as file:
    length_X, length_Y = map(int, file.readline().strip().split(" "))
    gap_cost, mismatch_cost = map(int, file.readline().strip().split(" "))
    X = file.readline().strip()
    Y = file.readline().strip()

def c(x, y):
    if x == y:
        return 0
    else:
        return mismatch_cost

dp = [[0] * (length_X + 1) for i in range(length_Y + 1)]

for j in range(length_X + 1):
    dp[0][j] = j * gap_cost

for k in range(length_Y + 1):
    dp[k][0] = k * gap_cost

for y in range(1, length_Y + 1):
    for x in range(1, length_X + 1):
        dp[y][x] = min(
            dp[y-1][x-1] + c(X[x-1], Y[y-1]),  
            dp[y-1][x] + gap_cost,             
            dp[y][x-1] + gap_cost              
        )

x = length_X
y = length_Y
X_alignment = []
Y_alignment = []

while x > 0 and y > 0:
    minimum = min(
            dp[y-1][x-1] + c(X[x-1], Y[y-1]),  
            dp[y-1][x] + gap_cost,             
            dp[y][x-1] + gap_cost              
    )
    
    if minimum == dp[y-1][x-1] + c(X[x-1], Y[y-1]):
        X_alignment.insert(0, X[x-1])
        Y_alignment.insert(0, Y[y-1])
        y -= 1
        x -= 1
    elif minimum == dp[y-1][x] + gap_cost:
        X_alignment.insert(0, "-")
        Y_alignment.insert(0, Y[y-1])
        y -= 1
    else:
        X_alignment.insert(0, X[x-1])
        Y_alignment.insert(0, "-")
        x -= 1

while x > 0:
    X_alignment.insert(0, X[x-1])
    Y_alignment.insert(0, "-")
    x -= 1

while y > 0:
    X_alignment.insert(0, "-")
    Y_alignment.insert(0, Y[y-1])
    x -= 1

print(dp[length_Y][length_X])
print(''.join(X_alignment))
print(''.join(Y_alignment))
