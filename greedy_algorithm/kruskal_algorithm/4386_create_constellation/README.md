## 4386번 별자리 만들기

---

시간 제한: 1초, 메모리 제한: 128MB

도현이는 우주의 신이다. 이제 도현이는 아무렇게나 널브러져 있는 n개의 별들을 이어서 별자리를 하나 만들 것이다. 별자리의 조건은 다음과 같다.

- 별자리를 이루는 선은 서로 다른 두 별을 일직선으로 이은 형태이다.
- 모든 별들은 별자리 위의 선을 통해 서로 직/간접적으로 이어져 있어야 한다.

별들이 2차원 평면 위에 놓여 있다. 선을 하나 이을 때마다 두 별 사이의 거리만큼의 비용이 든다고 할 때, 별자리를 만드는 최소 비용을 구하시오.

### 입력

- 첫째 줄에 별의 개수 n이 주어진다. (1 ≤ n ≤ 100)
- 둘째 줄부터 n개의 줄에 걸쳐 각 별의 x, y좌표가 실수 형태로 주어지며, 최대 소수점 둘째자리까지 주어진다. 좌표는 1000을 넘지 않는 양의 실수이다.

### 출력

- 첫째 줄에 정답을 출력한다. 절대/상대 오차는 10-2까지 허용한다.

---
~~~
import math

n = int(input())
stars = []
parent = [0]*n
for k in range(n):
    parent[k] = k
for _ in range(n):
    x, y = map(float, input().split())
    stars.append((x, y))

edges = []
for i in range(n-1):
    for j in range(i+1, n):
        cost = round(math.sqrt((stars[i][0]-stars[j][0])**2 + (stars[i][1]-stars[j][1])**2), 2)
        edges.append((cost, i, j))


def find_parent(x, p):
    if p[x] != x:
        p[x] = find_parent(p[x], p)
    return p[x]


def union_parent(a, b, p):
    a = find_parent(a, p)
    b = find_parent(b, p)
    if a < b:
        p[b] = a
    else:
        p[a] = b


edges.sort()
result = 0
for edge in edges:
    c, star_x, star_y = edge
    if find_parent(star_x, parent) != find_parent(star_y, parent):
        result += c
        union_parent(star_x, star_y, parent)
print(result)

~~~