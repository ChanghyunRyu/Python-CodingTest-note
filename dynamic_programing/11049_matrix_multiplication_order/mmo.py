import sys
INF = int(1e9)

n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, sys.stdin.readline().split())))

dp = [[INF]*n for _ in range(n)]
for i in range(n):
    dp[i][i] = 0

for d in range(1, n):
    for start in range(n-d):
        end = start+d
        for mid in range(start, end):
            dp[start][end] = min(dp[start][end], dp[start][mid]+dp[mid+1][end]+matrix[start][0]*matrix[mid][1]*matrix[end][1])

print(dp[0][n-1])
