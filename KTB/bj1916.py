import sys
INF = int(1e9)

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(m):
    start, end, price = map(int, sys.stdin.readline().split())
    graph[start][end] = min(graph[start][end], price)

s, e = map(int, sys.stdin.readline().split())
visited = [False]*(n+1)
graph[s][s] = 0

visited[s] = True
for _ in range(n-1):
    now = 0
    min_value = INF
    for i in range(1, n+1):
        if not visited[i] and min_value > graph[s][i]:
            now = i
            min_value = graph[s][i]
    visited[now] = True
    for j in range(1, n+1):
        if graph[s][now] + graph[now][j] < graph[s][j]:
            graph[s][j] = graph[s][now] + graph[now][j]

print(graph[s][e])
