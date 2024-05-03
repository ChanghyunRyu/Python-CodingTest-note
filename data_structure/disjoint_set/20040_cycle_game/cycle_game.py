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
parent = [0]*n
for i in range(1, n):
    parent[i] = i
result = 0
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    if find_parent(a, parent) == find_parent(b, parent):
        result = i+1
        break
    else:
        union_parent(a, b, parent)
print(result)
