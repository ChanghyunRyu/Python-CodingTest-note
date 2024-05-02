import math

n, m = map(int, input().split())
gods = [(0, 0)]
for _ in range(n):
    x, y = map(int, input().split())
    gods.append((x, y))
parent = [0]*(n+1)
for k in range(1, n+1):
    parent[k] = k

edges = []
for i in range(1, n):
    for j in range(i+1, n+1):
        cost = math.sqrt((gods[i][0]-gods[j][0])**2+(gods[i][1]-gods[j][1])**2)
        edges.append((cost, i, j))
edges.sort()


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


for _ in range(m):
    a, b = map(int, input().split())
    union_parent(a, b, parent)

result = 0
for edge in edges:
    c, god_a, god_b = edge
    if find_parent(god_a, parent) != find_parent(god_b, parent):
        result += c
        union_parent(god_a, god_b, parent)
print('{:.2f}'.format(result))
