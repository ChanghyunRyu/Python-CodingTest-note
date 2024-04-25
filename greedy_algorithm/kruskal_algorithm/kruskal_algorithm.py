v, e = map(int, input().split())
parent = [0]*(v+1)
for i in range(1, v+1):
    parent[i] = i

edges = []
result = 0

for _ in range(e):
    x, y, cost = map(int, input().split())
    edges.append((cost, x, y))
edges.sort()


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


for edge in edges:
    cost, a, b = edge
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        result += cost

print(result)
