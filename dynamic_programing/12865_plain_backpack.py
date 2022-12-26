import sys

n, k = map(int, input().split())
t = [(0, 0)]
for i in range(n):
    w, v = map(int, sys.stdin.readline().split())
    t.append((w, v))
d = [[0]*(k+1) for i in range(n+1)]
for i in range(1, n+1):
    for j in range(1, k+1):
        weight = t[i][0]
        value = t[i][1]

        if j < weight:
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i-1][j-weight] + value, d[i-1][j])
print(d[n][k])
