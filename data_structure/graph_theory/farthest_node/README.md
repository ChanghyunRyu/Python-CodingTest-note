## 가장 먼 노드

---

[출처] https://school.programmers.co.kr/learn/courses/30/lessons/49189

n개의 노드가 있는 그래프가 있습니다. 각 노드는 1부터 n까지 번호가 적혀있습니다. 
1번 노드에서 가장 멀리 떨어진 노드의 갯수를 구하려고 합니다. 
가장 멀리 떨어진 노드란 최단경로로 이동했을 때 간선의 개수가 가장 많은 노드들을 의미합니다.

노드의 개수 n, 간선에 대한 정보가 담긴 2차원 배열 vertex가 매개변수로 주어질 때,
1번 노드로부터 가장 멀리 떨어진 노드가 몇 개인지를 return 하도록 solution 함수를 작성해주세요.


### 제한 사항

- 노드의 개수 n은 2 이상 20,000 이하입니다.
- 간선은 양방향이며 총 1개 이상 50,000개 이하의 간선이 있습니다.
- vertex 배열 각 행 [a, b]는 a번 노드와 b번 노드 사이에 간선이 있다는 의미입니다.

---
### Problem Solved Check
- [x] 1회 24/06/26
- [ ] 2회
- [ ] 3회
~~~
from collections import deque
INF = int(1e6)


def solution(n, edge):
    indegree = [INF]*(n+1)
    graph = [[] for _ in range(n+1)]
    for start, end in edge:
        graph[start].append(end)
        graph[end].append(start)

    q = deque([1])
    indegree[1] = 1
    while q:
        now = q.popleft()
        for i in graph[now]:
            if indegree[i] == INF:
                indegree[i] = indegree[now]+1
                q.append(i)

    max_indegree = max(indegree[1:])
    answer = 0
    for i in range(1, n+1):
        if indegree[i] == max_indegree:
            answer += 1
    return answer
    
~~~
~~~
from collections import defaultdict
from collections import deque


def solution(n, vertex):
    graph = defaultdict(list)
    visited = [False]*(n+1)
    for v in vertex:
        start, end = v
        graph[start].append(end)
        graph[end].append(start)

    queue = deque([(1, 0)])
    answer = {}
    max_distance = 0
    while queue:
        now, distance = queue.popleft()
        if visited[now]:
            continue
        visited[now] = True
        max_distance = max(max_distance, distance)
        if distance in answer:
            answer[distance] += 1
        else:
            answer[distance] = 1
        for next_node in graph[now]:
            if not visited[next_node]:
                queue.append((next_node, distance + 1))
    return answer[max_distance]
    
~~~