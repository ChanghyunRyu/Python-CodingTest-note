import sys
from collections import deque

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False]*(n+1)
visited[1] = True
q = deque([1])
count = 0
while q:
    node = q.popleft()
    for i in graph[node]:
        if not visited[i]:
            count += 1
            visited[i] = True
            q.append(i)

print(count)
