import heapq
import sys
INF = int(1e9)

n, m, x = map(int, input().split())
path = [[] for i in range(n+1)]
path_reverse = [[] for i in range(n+1)]
for _ in range(m):
    start, end, t = map(int, sys.stdin.readline().split())
    path[start].append((end, t))
    path_reverse[end].append((start, t))


def dijkstra(start, graph):
    distance = [INF]*(n+1)
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        else:
            for g in graph[now]:
                cost = dist + g[1]
                if distance[g[0]] > cost:
                    distance[g[0]] = cost
                    heapq.heappush(q, (cost, g[0]))
    return distance


o2a = dijkstra(x, path)
a2o = dijkstra(x, path_reverse)
print(max([a2o[i] + o2a[i] for i in range(1,n+1) if i != x]))
