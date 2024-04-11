import sys
import heapq
INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for i in range(1+n)]
for _ in range(m):
    a, b, c = map(int,sys.stdin.readline().split())
    graph[a].append((b, c))


def dijkstra(start, g):
    distance = [INF]*(n+1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start, set([])))
    while q:
        dist, now, node_set = heapq.heappop(q)
        if dist < 0 and now in node_set:
            print(-1)
            return
        if distance[now] < dist:
            continue
        for next_node, dis in g[now]:
            cost = dist + dis
            if cost < distance[next_node]:
                node_set.add(now)
                node_set = set(node_set)
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node, node_set))
    for i in range(2, n+1):
        if distance[i] == INF:
            print(-1)
        else:
            print(distance[i])


dijkstra(1, graph)
