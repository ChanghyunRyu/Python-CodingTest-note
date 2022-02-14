# 백준 문제 1260번
# 4번이나 실패함, 처음 2번은 런타임 에러(BFS쪽 디자인을 잘못했던 것 같음 boundary 에러가 계속 일어남)
# BFS 디자인 쪽 복습이 필요해 보임
from collections import deque


n, m, start = map(int, input().split())
graph = [[] for i in range(n+1)]
for i in range(m):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)
for i in range(n+1):
    graph[i].sort()


def DFS(graph, i, visited, list):
    visited[i-1] = True
    list.append(i)
    nodes = graph[i]
    for node in nodes:
        if not visited[node - 1]:
            DFS(graph, node, visited, list)


def BFS(graph, start, visited, list):
    queue = deque([start])
    visited[start-1] = True
    while queue:
        v = queue.popleft()
        list.append(v)
        for i in graph[v]:
            if not visited[i-1]:
                queue.append(i)
                visited[i-1] = True


list_DFS = []
list_BFS = []
visited = [False for i in range(n)]
DFS(graph, start, visited, list_DFS)
node_queue = deque()
node_queue.append(start)
visited = [False for i in range(n)]
BFS(graph, start, visited, list_BFS)
for node in list_DFS:
    print(node, end=' ')
print()
for node in list_BFS:
    print(node, end=' ')


