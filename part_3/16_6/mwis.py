w = [0]

with open("problem16_6.txt") as file:
    n = int(file.readline().strip())
    for line in file:
        w.append(int(line.strip()))
        


A = [w[0],w[1]]
for i in range(2, n + 1):
    A.append(max(A[i-1], A[i-2] + w[i]))


S = []
j = n
while j >= 2:
    if A[j-1] >= A[j-2] + w[j]:
        j -= 1
    else:
        S.append(j)
        j -= 2
if j == 1:
    S.append(1)

print(A[n])
print(S)
