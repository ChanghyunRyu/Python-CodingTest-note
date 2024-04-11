import sys
INF = int(1e9)

v, e = map(int, input().split())
graph = [[INF]*(v+1) for _ in range(v+1)]

for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a][b] = c

for i in range(1, v+1):
    for j in range(1, v+1):
        for k in range(1, v+1):
            graph[j][k] = min(graph[j][i]+graph[i][k], graph[j][k])

result = min([graph[i][i] for i in range(1, v+1)])

if result >= INF:
    print(-1)
else:
    print(result)
