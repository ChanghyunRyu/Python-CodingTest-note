## 4195번 친구 네트워크

---

시간 제한: 3초, 메모리 제한: 256MB

민혁이는 소셜 네트워크 사이트에서 친구를 만드는 것을 좋아하는 친구이다. 우표를 모으는 취미가 있듯이, 민혁이는 소셜 네트워크 사이트에서 친구를 모으는 것이 취미이다.

어떤 사이트의 친구 관계가 생긴 순서대로 주어졌을 때, 두 사람의 친구 네트워크에 몇 명이 있는지 구하는 프로그램을 작성하시오.

친구 네트워크란 친구 관계만으로 이동할 수 있는 사이를 말한다.

### 입력

- 첫째 줄에 테스트 케이스의 개수가 주어진다. 
- 각 테스트 케이스의 첫째 줄에는 친구 관계의 수 F가 주어지며, 이 값은 100,000을 넘지 않는다. 
- 다음 F개의 줄에는 친구 관계가 생긴 순서대로 주어진다. 
- 친구 관계는 두 사용자의 아이디로 이루어져 있으며, 알파벳 대문자 또는 소문자로만 이루어진 길이 20 이하의 문자열이다.

### 출력

- 친구 관계가 생길 때마다, 두 사람의 친구 네트워크에 몇 명이 있는지 구하는 프로그램을 작성하시오.

---
기존 유니온-파인드 문제와 다르게 문자열로 입력받기 때문에 dictionary 자료형을 사용해야 한다.  
문자열과의 비교도 물론 가능이야 하지만 그보다는 사이즈가 더 큰 쪽을 부모로 선정하게 하는게 나을 것 같아 그런 방향으로 구현했다.
~~~
import sys
sys.setrecursionlimit(10**6)


def find_parent(x, p):
    if p[x] != x:
        p[x] = find_parent(p[x], p)
    return p[x]


def union_parent(a, b, p, s):
    a = find_parent(a, p)
    b = find_parent(b, p)
    if a == b:
        return s[a]
    else:
        if s[a] < s[b]:
            p[a] = b
            s[b] += s[a]
            return s[b]
        else:
            p[b] = a
            s[a] += s[b]
            return s[a]


t = int(input())
for _ in range(t):
    f = int(sys.stdin.readline().rstrip())
    parent = dict()
    union_size = dict()
    for _ in range(f):
        name1, name2 = sys.stdin.readline().split()
        if name1 not in parent:
            parent[name1] = name1
            union_size[name1] = 1
        if name2 not in parent:
            parent[name2] = name2
            union_size[name2] = 1
        result = union_parent(name1, name2, parent, union_size)
        print(result)

~~~