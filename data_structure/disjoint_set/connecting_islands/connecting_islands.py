def solution(n, costs):
    answer = 0
    costs = sorted(costs, key=lambda x: x[2])
    parent = [i for i in range(n)]
    for start, end, costs in costs:
        if find_parent(start, parent) != find_parent(end, parent):
            answer += costs
            union_parent(start, end, parent)
    return answer


def find_parent(x, parent):
    if parent[x] != x:
        parent[x] = find_parent(parent[x], parent)
    return parent[x]


def union_parent(a, b, parent):
    a = find_parent(a, parent)
    b = find_parent(b, parent)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))
