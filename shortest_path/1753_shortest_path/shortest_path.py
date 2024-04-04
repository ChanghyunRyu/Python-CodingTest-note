import sys
import heapq
INF = int(1e9)

n, e = map(int, input().split())
k = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(e):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))


def shortest_path(start, graph):
    distance = [INF]*(n+1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        else:
            for i in graph[now]:
                cost = dist + i[1]
                if distance[i[0]] > cost:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))
    return distance


shortest_path = shortest_path(k, graph)
for i in range(1, n+1):
    if shortest_path[i] == INF:
        print('INF')
    else:
        print(shortest_path[i])
