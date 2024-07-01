from collections import deque
INF = int(1e6)


def solution(n, edge):
    indegree = [INF]*(n+1)
    graph = [[] for _ in range(n+1)]
    for start, end in edge:
        graph[start].append(end)
        graph[end].append(start)

    q = deque([1])
    indegree[1] = 1
    while q:
        now = q.popleft()
        for i in graph[now]:
            if indegree[i] == INF:
                indegree[i] = indegree[now]+1
                q.append(i)

    max_indegree = max(indegree[1:])
    answer = 0
    for i in range(1, n+1):
        if indegree[i] == max_indegree:
            answer += 1
    return answer


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
