import sys
sys.setrecursionlimit(10**6)

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

count = 1
visit = [0]*(n+1)


def dfs(node):
    global count
    visit[node] = count
    graph[node].sort(reverse=True)
    for i in graph[node]:
        if visit[i] == 0:
            count += 1
            dfs(i)


dfs(r)
for j in range(1, n+1):
    print(visit[j])
