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
