## 1717번 집합의 표현

---

시간 제한: 2초, 메모리 제한: 128MB

초기에 (n+1)개의 집합 {0}, {1}, {2},...,{n}이 있다. 여기에 합집합 연산과, 두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산을 수행하려고 한다.

집합을 표현하는 프로그램을 작성하시오.

### 입력

- 첫째 줄에 n, m이 주어진다. m은 입력으로 주어지는 연산의 개수이다. 다음 m개의 줄에는 각각의 연산이 주어진다.
- 합집합은 0 a b의 형태로 입력이 주어진다. 이는 a가 포함되어 있는 집합과, b가 포함되어 있는 집합을 합친다는 의미이다.
- 두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산은 1 a b의 형태로 주어진다.
- 1 ≤ n ≤ 1,000,000
- 1 ≤ m ≤ 100,000

### 출력

- 1로 시작하는 입력에 대하여 a와 b가 같은 집합에 포함되어 있으면 "YES"또는 "yes"를, 그렇지 않다면 "NO"또는 "no"를 한줄에 하나씩 출력한다.

---
~~~
import sys
sys.setrecursionlimit(10**6)


def find_parent(x, p):
    if p[x] != x:
        p[x] = find_parent(p[x], p)
    return p[x]


def union_parent(x, y, p):
    x = find_parent(x, p)
    y = find_parent(y, p)
    if x < y:
        p[y] = x
    else:
        p[x] = y


n, m = map(int, input().split())
parent = [0]*(n+1)
for i in range(n+1):
    parent[i] = i
for _ in range(m):
    check, a, b = map(int, sys.stdin.readline().split())
    if check == 0:
        union_parent(a, b, parent)
    else:
        if find_parent(a, parent) != find_parent(b, parent):
            print("NO")
        else:
            print("YES")

~~~
