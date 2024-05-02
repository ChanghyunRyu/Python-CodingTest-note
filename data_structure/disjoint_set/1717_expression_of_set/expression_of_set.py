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
