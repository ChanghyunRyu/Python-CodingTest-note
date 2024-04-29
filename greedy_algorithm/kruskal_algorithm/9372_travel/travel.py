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