import heapq

v, e = map(int, input().split())
visited = [False]*(v+1)
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
    graph[b].append((a, cost))

q = []
start = 1
heapq.heappush(q, (0, start))
result = 0
while q:
    cost, now = heapq.heappop(q)
    if not visited[now]:
        visited[now] = True
        result += cost
        for i in graph[now]:
            if not visited[i[0]]:
                heapq.heappush(q, (i[1], i[0]))
print(result)
