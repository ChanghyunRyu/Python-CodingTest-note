### Dijkstar.py

다익스트라 알고리즘을 간단하게 구현하는 방법.  
구현은 간단하지만 시간복잡도가 O(V^2)로 매우 높다.(V는 노드의 개수)

~~~
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n+1)]
visited = [False]*(n+1)  # 노드를 방문한 적 있는지 체크
distance = [INF]*(n+1)  # 최단 거리 테이블을 모두 무한으로 초기화

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def get_smallest_node():
    min_value =INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost


dijkstra(start)
for i in range(1, n+1):
    if distance[i] == INF:
        print('Impossible', end=' ')
    else:
        print(distance[i], end=' ')

~~~

---

### Dijkstar2.py

위에서 구현한 다익스트라 알고리즘은 구현은 간단하지만 실행 속도가 느리다는 단점을 가지고 있다.  
실행 속도가 느린 이유는 마지막에 탐색한 노드에서 가장 거리가 가까운 노드를 구하는 데 O(V)만큼의 시간이 걸리기 때문이다.  

이점을 개선하기 위하여 다음 구현에서는 우선순위 큐 자료구조를 사용한다.  
해당 방법으로 구현된 다익스트라 알고리즘의 시간복잡도는 O(ElogV)이다. (E는 간선 개수, V는 노드 개수)

[**우선 순위 큐에 대한 자세한 설명**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/queue%26heap)

~~~
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n+1)]
distance = [INF]*(n+1)  # 최단 거리 테이블을 모두 무한으로 초기화

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)
for i in range(1, n+1):
    if distance[i] == INF:
        print('Impossible', end=' ')
    else:
        print(distance[i], end=' ')

~~~
