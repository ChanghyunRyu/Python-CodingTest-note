# 내일 다시 풀어봐라!
# 아예 생각을 못 했는데요? 씹
import sys
n, k = map(int, input().split())
things = [(0, 0)]
for i in range(n):
    w, v = map(int, sys.stdin.readline().split())
    things.append((w, v))

d = [[0]*(k+1) for i in range(n+1)]
for i in range(1, n+1):
    for j in range(1, k+1):
        weight = things[i][0]
        value = things[i][1]

        if j < weight:
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i-1][j-weight] + value, d[i-1][j])
print(d[n][k])
