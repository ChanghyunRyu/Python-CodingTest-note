## 9372번 상근이의 여행

---

시간 제한: 1초, 메모리 제한: 256MB

상근이는 겨울방학을 맞아 N개국을 여행하면서 자아를 찾기로 마음먹었다. 

하지만 상근이는 새로운 비행기를 무서워하기 때문에, 최대한 적은 종류의 비행기를 타고 국가들을 이동하려고 한다.

이번 방학 동안의 비행 스케줄이 주어졌을 때, 상근이가 가장 적은 종류의 비행기를 타고 모든 국가들을 여행할 수 있도록 도와주자.

상근이가 한 국가에서 다른 국가로 이동할 때 다른 국가를 거쳐 가도(심지어 이미 방문한 국가라도) 된다.

### 입력

- 첫 번째 줄에는 테스트 케이스의 수 T(T ≤ 100)가 주어지고,
- 각 테스트 케이스마다 다음과 같은 정보가 주어진다.
- 첫 번째 줄에는 국가의 수 N(2 ≤ N ≤ 1 000)과 비행기의 종류 M(1 ≤ M ≤ 10 000) 가 주어진다.
- 이후 M개의 줄에 a와 b 쌍들이 입력된다. a와 b를 왕복하는 비행기가 있다는 것을 의미한다. (1 ≤ a, b ≤ n; a ≠ b) 
- 주어지는 비행 스케줄은 항상 연결 그래프를 이룬다.

### 출력

- 테스트 케이스마다 한 줄을 출력한다.
- 상근이가 모든 국가를 여행하기 위해 타야 하는 비행기 종류의 최소 개수를 출력한다.

---
해당 문제는 dfs를 이용하여 풀이해도 되지만, 최소 신장트리 알고리즘인 크루스칼 알고리즘을 이용하여 구현하였다.
~~~
import sys


def find_parent(x, p):
    if p[x] != x:
        p[x] = find_parent(p[x], p)
    return p[x]


def union_parent(node_x, node_y, p):
    node_x = find_parent(node_x, p)
    node_y = find_parent(node_y, p)
    if node_x < node_y:
        p[node_y] = node_x
    else:
        p[node_x] = node_y


t = int(input())
result = []
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    parent = [0]*(n+1)
    for i in range(1, n+1):
        parent[i] = i
    edges = []
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        edges.append((a, b))

    cnt = 0
    for e in edges:
        x, y = e
        if find_parent(x, parent) != find_parent(y, parent):
            cnt += 1
            union_parent(x, y, parent)
    result.append(cnt)

for r in result:
    print(r)
~~~