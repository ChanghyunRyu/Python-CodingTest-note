# DFS(Depth-First-Search): 깊이 우선 탐색
# 1. 탐색 시작 노드를 스택에 삽입하여 방문 처리.
# 2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 인접 노드를 스택에 넣고 방문처리.
# 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
# 3. 2번 과정을 더 수행할 수 없을 때까지 반복.
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


