## 1504번 특정한 최단 경로

---

시간 제한: 1초, 메모리 제한: 256 MB

방향성이 없는 그래프가 주어진다. 세준이는 1번 정점에서 N번 정점으로 최단 거리로 이동하려고 한다. 또한 세준이는 두 가지 조건을 만족하면서 이동하는 특정한 최단 경로를 구하고 싶은데, 그것은 바로 임의로 주어진 두 정점은 반드시 통과해야 한다는 것이다.

세준이는 한번 이동했던 정점은 물론, 한번 이동했던 간선도 다시 이동할 수 있다. 하지만 반드시 최단 경로로 이동해야 한다는 사실에 주의하라. 1번 정점에서 N번 정점으로 이동할 때, 주어진 두 정점을 반드시 거치면서 최단 경로로 이동하는 프로그램을 작성하시오.

### 입력

- 첫째 줄에 정점의 개수 N과 간선의 개수 E가 주어진다. (2 ≤ N ≤ 800, 0 ≤ E ≤ 200,000) 
- 둘째 줄부터 E개의 줄에 걸쳐서 세 개의 정수 a, b, c가 주어지는데, a번 정점에서 b번 정점까지 양방향 길이 존재하며, 그 거리가 c라는 뜻이다. (1 ≤ c ≤ 1,000)
- 다음 줄에는 반드시 거쳐야 하는 두 개의 서로 다른 정점 번호 v1과 v2가 주어진다. (v1 ≠ v2, v1 ≠ N, v2 ≠ 1) 임의의 두 정점 u와 v사이에는 간선이 최대 1개 존재한다.

### 출력

- 첫째 줄에 두 개의 정점을 지나는 최단 경로의 길이를 출력한다. 
- 그러한 경로가 없을 때에는 -1을 출력한다.

---

~~~
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

~~~
