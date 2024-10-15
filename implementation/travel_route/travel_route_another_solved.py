from collections import defaultdict


def solution(tickets):
    graph = defaultdict(list)
    for start, end in tickets:
        graph[start].append(end)
    for key in graph.keys():
        graph[key].sort(reverse=True)

    return dfs(['ICN'], graph, [])


def dfs(path, graph, visited):
    if path:
        now = path[-1]
        if graph[now]:
            path.append(graph[now].pop())
        else:
            visited.append(path.pop())
        dfs(path, graph, visited)

    return visited[::-1]


print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
