## 1707번 이분 그래프

---

시간 제한: 2초, 메모리 제한: 256MB

그래프의 정점의 집합을 둘로 분할하여, 각 집합에 속한 정점끼리는 서로 인접하지 않도록 분할할 수 있을 때, 그러한 그래프를 특별히 이분 그래프 (Bipartite Graph) 라 부른다.

그래프가 입력으로 주어졌을 때, 이 그래프가 이분 그래프인지 아닌지 판별하는 프로그램을 작성하시오.

### 입력

- 입력은 여러 개의 테스트 케이스로 구성되어 있는데, 첫째 줄에 테스트 케이스의 개수 K가 주어진다.
- 각 테스트 케이스의 첫째 줄에는 그래프의 정점의 개수 V와 간선의 개수 E가 빈 칸을 사이에 두고 순서대로 주어진다. 
- 각 정점에는 1부터 V까지 차례로 번호가 붙어 있다. 
- 이어서 둘째 줄부터 E개의 줄에 걸쳐 간선에 대한 정보가 주어지는데, 각 줄에 인접한 두 정점의 번호 u, v (u ≠ v)가 빈 칸을 사이에 두고 주어진다. 
- 2 ≤ K ≤ 5, 1 ≤ V ≤ 20,000, 1 ≤ E ≤ 200,000

### 출력

- K개의 줄에 걸쳐 입력으로 주어진 그래프가 이분 그래프이면 YES, 아니면 NO를 순서대로 출력한다.

---
### 이분 그래프

이분 그래프는 그래프 형태의 자료구조로 정점을 2그룹으로 나눌 수 있으며 같은 그룹의 정점끼리는 간선으로 이어지지 않은 경우를 의미한다. 

이분 그래프를 판단하는 문제는 BFS, DFS로 간단하게 구현할 수 있다.

1. 최초 탐색 시작할 정점을 색상1로 칠한다.
2. 최초 정점의 인접 정점의 색상을 색상2로 칠한다.
3. 인접 정점들을 탐색하며 위의 과정을 반복한다.
4. 탐색 도중 인접 정점이 같은 색으로 칠해져 있다면 이분 그래프가 될 수 없는 것이다.

**단, 그래프의 모든 노드가 이어지지 않은 경우가 있을 수 있으므로 해당 부분을 확인하고 구현해야 한다.**

~~~
import sys
from collections import deque


def dfs(g):
    check = [0]*(v+1)
    q = deque([])
    for i in range(1, v+1):
        q.append((i, 1))
    while q:
        now, color = q.pop()
        if check[now] == 0:
            check[now] = color
        for i in g[now]:
            if check[i] == 0:
                q.append((i, -color))
            elif check[i] == check[now]:
                return 'NO'
    return 'YES'


k = int(input())
result = []
for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        u, w = map(int , sys.stdin.readline().split())
        graph[u].append(w)
        graph[w].append(u)
    result.append(dfs(graph))

for r in result:
    print(r)

~~~