import sys


def find_parent(s, p):
    if p[s] != s:
        p[s] = find_parent(p[s], p)
    return p[s]


def union_parent(a, b, p):
    a = find_parent(a, p)
    b = find_parent(b, p)
    if a < b:
        p[b] = a
    else:
        p[a] = b


while True:
    line = list(map(int, sys.stdin.readline().split()))
    if line[0] == 0 and line[1] == 0:
        break
    else:
        m, n = line[0], line[1]
        edges = []
        parent = [0] * m
        for i in range(m):
            parent[i] = i

        all_sum = 0
        for _ in range(n):
            x, y, z = map(int, sys.stdin.readline().split())
            edges.append((z, x, y))
            all_sum += z
        edges.sort()

        answer = 0
        for edge in edges:
            cost, node_x, node_y = edge
            if find_parent(node_x, parent) != find_parent(node_y, parent):
                answer += cost
                union_parent(node_x, node_y, parent)
        print(all_sum - answer)
