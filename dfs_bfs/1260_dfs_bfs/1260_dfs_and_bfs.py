import sys
from collections import deque


def dfs(graph, v, visited, result):
    result.append(v)
    visited[v] = True
    for g in graph[v]:
        if not visited[g]:
            dfs(graph, g, visited, result)


def bfs(graph, v, visited):
    result = []
    visited[v] = True
    queue = deque([v])

    while queue:
        n = queue.popleft()
        result.append(n)
        for g in graph[n]:
            if not visited[g]:
                visited[g] = True
                queue.append(g)

    return result


n, m, start = map(int, input().split())

graph = [[] for i in range(n+1)]
visited = [False]*(n+1)

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    graph[i].append(j)
    graph[j].append(i)
for g in graph:
    g.sort()

result = []
dfs(graph, start, visited, result)
for i in result:
    print(i, end=' ')
print()
visited = [False]*(n+1)
result = bfs(graph, start, visited)
for i in result:
    print(i, end=' ')
print()
