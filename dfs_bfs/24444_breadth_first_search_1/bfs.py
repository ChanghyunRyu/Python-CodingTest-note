import sys
from collections import deque

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

count = 1
visit = [0]*(n+1)
visit[r] = 1
q = deque([r])
while q:
    node = q.popleft()
    graph[node].sort()
    for i in graph[node]:
        if visit[i] == 0:
            count += 1
            visit[i] = count
            q.append(i)


for j in range(1, n+1):
    print(visit[j])
