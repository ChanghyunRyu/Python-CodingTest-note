import sys
INF = int(1e9)

v, e = map(int, input().split())
graph = []
distance = [INF]*(v+1)

for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph.append((a, b, c))

start = 1
negative_cycle = False

distance[start] = 0
for i in range(v):
    for start_node, next_node, cost in graph:
        if distance[start_node] != INF and distance[next_node] > distance[start_node] + cost:
            distance[next_node] = distance[start_node]+cost
            if i == v-1:
                negative_cycle = True

if negative_cycle:
    print(-1)
else:
    for i in range(2, v+1):
        if distance[i] == INF:
            print(-1)
        else:
            print(distance[i])
