v, e = map(int, input().split())
parent = [0]*(v+1)
for i in range(1, v+1):
    parent[i] = i


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


check = False
for _ in range(e):
    x, y = map(int, input().split())
    if find_parent(x) == find_parent(y):
        check = True
        break
    else:
        union_parent(x, y)

if check:
    print('사이클이 발생했습니다.')
else:
    print('사이클이 발생하지 않았습니다.')
