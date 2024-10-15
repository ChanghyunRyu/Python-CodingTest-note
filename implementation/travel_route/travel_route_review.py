from collections import defaultdict
from collections import deque
from copy import deepcopy


def solution(tickets):
    answer = []
    graph = defaultdict(list)
    for start, end in tickets:
        graph[start].append(end)
    for g in graph:
        graph[g].sort()

    q = deque([('ICN', [], graph)])
    while q:
        now, result, g = q.popleft()
        result.append(now)
        if len(result) == len(tickets)+1:
            answer = result
            break

        next_cities = g[now]
        for i in range(len(next_cities)):
            new_arr = list(next_cities)
            new_graph = deepcopy(g)
            del new_arr[i]
            new_graph[now] = new_arr
            q.append((next_cities[i], list(result), new_graph))
    return answer

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
