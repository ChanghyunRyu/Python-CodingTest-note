from collections import deque

def bfs(graph, v, visted):
    queue = deque([v])
    visted[v] = True
    while queue:
        n = queue.popleft()
        print(n, end=' ')
        for g in graph[n]:
            if not visted[g]:
                queue.append(g)
                visted[g] = True


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
visted = [False]*9

bfs(graph, 1, visted)
