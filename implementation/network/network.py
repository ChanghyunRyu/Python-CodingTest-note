import sys
sys.setrecursionlimit(int(1e6))


def find_parent(x, parent):
    if parent[x] != x:
        parent[x] = find_parent(parent[x], parent)
    return parent[x]


def union_parent(x, y, parent):
    x = find_parent(x, parent)
    y = find_parent(y, parent)
    if x > y:
        parent[x] = y
    else:
        parent[y] = x


def solution(n, computers):
    parents = list(range(n))
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if computers[i][j] == 1:
                union_parent(i, j, parents)
    result = set()
    for parent in parents:
        result.add(find_parent(parent, parents))
    return len(result)


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
print(solution(3, [[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
print(solution(5, [[1,1,0,1,0], [1, 1, 0, 0, 0], [0,0,1,0,1], [1,0,0,1,1], [0,0,1,1,1]]))
