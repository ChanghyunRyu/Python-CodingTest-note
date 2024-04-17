import sys
from collections import deque


def bfs(x, y, count, graph):
    q = deque([(x, y)])
    nx = len(graph)
    ny = len(graph[0])
    while q:
        node_x, node_y = q.popleft()
        if node_x-1 >= 0 and graph[node_x-1][node_y] == 1:
            graph[node_x-1][node_y] = count
            q.append((node_x-1, node_y))
        if node_x+1 < nx and graph[node_x+1][node_y] == 1:
            graph[node_x+1][node_y] = count
            q.append((node_x+1, node_y))
        if node_y-1 >= 0 and graph[node_x][node_y-1] == 1:
            graph[node_x][node_y-1] = count
            q.append((node_x, node_y-1))
        if node_y+1 < ny and graph[node_x][node_y+1] == 1:
            graph[node_x][node_y+1] = count
            q.append((node_x, node_y+1))


T = int(input())
result = []
for _ in range(T):
    n, m, k = map(int, input().split())
    field = [[0]*m for _ in range(n)]
    c = 2
    for _ in range(k):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        field[a][b] = 1
    for i in range(n):
        for j in range(m):
            if field[i][j] == 1:
                bfs(i, j, c, field)
                c += 1
    result.append(c-2)

for r in result:
    print(r)
