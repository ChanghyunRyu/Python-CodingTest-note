from collections import defaultdict


def solution(edges):
    answer = [0]*4
    in_graph = defaultdict(list)
    out_graph = defaultdict(list)
    for a, b in edges:
        in_graph[b].append(a)
        out_graph[a].append(b)

    # root 찾기
    root = 0
    for node in out_graph:
        if node not in in_graph and len(out_graph[node]) >= 2:
            root = node
            break
    answer[0] = root

    v = {root}
    for node in in_graph:
        if node in v:
            continue
        shape = dfs(node, v, in_graph, out_graph)
        if shape == 'donut':
            answer[1] += 1
        elif shape == 'stick':
            answer[2] += 1
        elif shape == 'eight':
            answer[3] += 1
    return answer


def dfs(node, visited, in_graph, out_graph):
    s = [node]
    shape = 'donut'
    while s:
        now = s.pop()
        visited.add(now)
        check = now in in_graph and now in out_graph
        if check and len(in_graph[now]) >= 2 and len(out_graph[now]) == 2:
            shape = 'eight'
        if now not in in_graph or now not in out_graph:
            shape = 'stick'
        if now in in_graph:
            next_nodes = in_graph[now]
            for next_node in next_nodes:
                if next_node not in visited:
                    s.append(next_node)
        if now in out_graph:
            next_nodes = out_graph[now]
            for next_node in next_nodes:
                if next_node not in visited:
                    s.append(next_node)
    return shape


e1 = [[2, 3], [4, 3], [1, 1], [2, 1]]
e2 = [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]
print(solution(e1))
print(solution(e2))
