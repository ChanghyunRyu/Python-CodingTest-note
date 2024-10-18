from collections import defaultdict
from collections import deque


def solution(n, vertex):
    graph = defaultdict(list)
    for start, end in vertex:
        graph[start].append(end)
        graph[end].append(start)

    q = deque([(1, 0)])
    visited = [False] * (n + 1)

    max_dis = 0
    distance = defaultdict(list)
    while q:
        now, count = q.popleft()
        if visited[now]:
            continue
        visited[now] = True
        distance[count].append(now)
        max_dis = max(max_dis, count)
        for next_node in graph[now]:
            if visited[next_node]:
                continue
            q.append((next_node, count + 1))
    return len(distance[max_dis])


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
