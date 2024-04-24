import sys
from collections import deque


def dfs(g):
    check = [0]*(v+1)
    q = deque([])
    for i in range(1, v+1):
        q.append((i, 1))
    while q:
        now, color = q.pop()
        if check[now] == 0:
            check[now] = color
        for i in g[now]:
            if check[i] == 0:
                q.append((i, -color))
            elif check[i] == check[now]:
                return 'NO'
    return 'YES'


k = int(input())
result = []
for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        u, w = map(int , sys.stdin.readline().split())
        graph[u].append(w)
        graph[w].append(u)
    result.append(dfs(graph))

for r in result:
    print(r)
