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
