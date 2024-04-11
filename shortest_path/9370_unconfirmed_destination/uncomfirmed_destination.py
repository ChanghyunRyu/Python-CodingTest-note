import sys
import heapq
INF = int(1e9)

test = int(input())
result = []
for _ in range(test):
    n, m, t = map(int, sys.stdin.readline().split())
    s, g, h = map(int, sys.stdin.readline().split())

    graph = [[] for i in range(n+1)]
    for _ in range(m):
        a, b, d = map(int, sys.stdin.readline().split())
        graph[a].append((b, d))
        graph[b].append((a, d))

    candidate = []
    for _ in range(t):
        candidate.append(int(sys.stdin.readline().rstrip()))

    distance = [INF] * (n + 1)
    r = [False] * (n + 1)
    q = []
    heapq.heappush(q, (0, s, False))
    while q:
        dist, now, check = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for next_node, dis in graph[now]:
            cost = dist + dis
            now_check = check or ((next_node == g and now == h) or (next_node == h and now == g))
            if cost < distance[next_node]:
                distance[next_node] = cost
                r[next_node] = now_check
                heapq.heappush(q, (cost, next_node, now_check))
            if not r[next_node] and cost == distance[next_node]:
                r[next_node] = now_check
                heapq.heappush(q, (cost, next_node, now_check))

    final = []
    for c in candidate:
        if r[c]:
            final.append(c)
    final.sort()
    result.append(final)

for i in result:
    for j in i:
        print(j, end=' ')
    print()
