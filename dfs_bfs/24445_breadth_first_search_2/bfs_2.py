import sys
from collections import deque

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

q = deque([r])
visit = [0]*(n+1)
visit[r] = 1
count = 2
while q:
    node = q.popleft()
    graph[node].sort(reverse=True)
    for g in graph[node]:
        if visit[g] == 0:
            visit[g] = count
            count += 1
            q.append(g)

for i in range(1, n+1):
    print(visit[i])
