def dfs(graph, v, visted):
    visted[v] = True
    print(v)
    for g in graph[v]:
        if visted[g] is False:
            dfs(graph, g, visted)


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

dfs(graph, 1, visted)
