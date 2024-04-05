import sys
import heapq
INF = int(1e9)

n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
graph_reverse = [[] for _ in range(n+1)]
for _ in range(e):
    start, end, dist = map(int, sys.stdin.readline().split())
    graph[start].append((end, dist))
    graph[end].append((start, dist))

v1, v2 = map(int, input().split())


def dijkstra(s, graph):
    distance = [INF]*(n+1)
    q = []
    heapq.heappush(q, (0, s))
    while q:
        dis, now = heapq.heappop(q)
        if distance[now] < dis:
            continue
        else:
            for i in graph[now]:
                cost = dis + i[1]
                if distance[i[0]] > cost:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))
    return distance


distance_start = dijkstra(1, graph)
distance_end = dijkstra(n, graph)
distance_mid = dijkstra(v1, graph)
distance_mid2 = dijkstra(v2, graph)
if v1 == 1 and v2 == n:
    result = distance_start[n]
elif v1 == 1:
    result = distance_start[v2] + distance_end[v2]
elif v2 == n:
    result = distance_start[v1] + distance_end[v1]
else:
    result = min(distance_start[v1]+distance_mid[v2]+distance_end[v2], distance_start[v2]+ distance_mid2[v1]+distance_end[v1])
if result >= INF:
    print(-1)
else:
    print(result)
