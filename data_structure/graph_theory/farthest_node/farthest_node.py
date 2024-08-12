from collections import defaultdict
from collections import deque


def solution(n, vertex):
    graph = defaultdict(list)
    visited = [False]*(n+1)
    for v in vertex:
        start, end = v
        graph[start].append(end)
        graph[end].append(start)

    queue = deque([(1, 0)])
    answer = {}
    max_distance = 0
    while queue:
        now, distance = queue.popleft()
        if visited[now]:
            continue
        visited[now] = True
        max_distance = max(max_distance, distance)
        if distance in answer:
            answer[distance] += 1
        else:
            answer[distance] = 1
        for next_node in graph[now]:
            if not visited[next_node]:
                queue.append((next_node, distance + 1))
    return answer[max_distance]


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
