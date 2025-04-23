n, m = map(int, input().split())

matrix = [[0]*m for _ in range(n)]
for i in range(2*n):
    temp = list(map(int, input().split()))
    for j in range(m):
        matrix[i % n][j] += temp[j]


for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()
