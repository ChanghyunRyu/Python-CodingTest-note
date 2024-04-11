## 타임머신

---

시간 제한: 1초, 메모리 제한: 256MB

N개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 버스가 M개 있다. 각 버스는 A, B, C로 나타낼 수 있는데, A는 시작도시, B는 도착도시, C는 버스를 타고 이동하는데 걸리는 시간이다. 시간 C가 양수가 아닌 경우가 있다. C = 0인 경우는 순간 이동을 하는 경우, C < 0인 경우는 타임머신으로 시간을 되돌아가는 경우이다.

1번 도시에서 출발해서 나머지 도시로 가는 가장 빠른 시간을 구하는 프로그램을 작성하시오.

### 입력

- 첫째 줄에 도시의 개수 N (1 ≤ N ≤ 500), 버스 노선의 개수 M (1 ≤ M ≤ 6,000)이 주어진다.
- 둘째 줄부터 M개의 줄에는 버스 노선의 정보 A, B, C (1 ≤ A, B ≤ N, -10,000 ≤ C ≤ 10,000)가 주어진다. 

### 출력

- 만약 1번 도시에서 출발해 어떤 도시로 가는 과정에서 시간을 무한히 오래 전으로 되돌릴 수 있다면 첫째 줄에 -1을 출력한다. 
- 그렇지 않다면 N-1개 줄에 걸쳐 각 줄에 1번 도시에서 출발해 2번 도시, 3번 도시, ..., N번 도시로 가는 가장 빠른 시간을 순서대로 출력한다. 
- 만약 해당 도시로 가는 경로가 없다면 대신 -1을 출력한다.

---
해당 문제는 단순히 벨만-포드 알고리즘을 구현하면 되는 문제이다.

~~~
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
~~~

다음은 해당 문제를 다익스트라 알고리즘으로 풀려고 했으나 실패한 경우이다.

출력 자체는 제대로 출력하나 특정 케이스에서 음수 사이클을 발견할 때 시행횟수가 너무 늘어나 시간 초과로 실패한다.

~~~
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

~~~
