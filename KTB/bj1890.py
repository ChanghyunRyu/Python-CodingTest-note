n = int(input())
jump = []
for _ in range(n):
    jump.append(list(map(int, input().split())))
dp = [[0]*n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if jump[i][j] == 0:
            break
        k = jump[i][j]
        if i+k < n:
            dp[i+k][j] += dp[i][j]
        if j+k < n:
            dp[i][j+k] += dp[i][j]

print(dp[n-1][n-1])
