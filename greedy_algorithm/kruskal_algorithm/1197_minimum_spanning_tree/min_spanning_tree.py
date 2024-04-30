import sys

v, e = map(int, input().split())
edges = []
parent = [0]*(v+1)
for i in range(1, v+1):
    parent[i] = i
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    edges.append((c, a, b))
edges.sort()


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


result = 0
for edge in edges:
    cost, node_x, node_y = edge
    if find_parent(node_x, parent) != find_parent(node_y, parent):
        result += cost
        union_parent(node_x, node_y, parent)
print(result)
