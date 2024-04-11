import sys
sys.setrecursionlimit(10**6)

n, m, r = map(int, input().split())
graph = [[] for _ in range(1+n)]
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

result = [0]*(n+1)
count = 1


def dfs(now):
    global count
    result[now] = count
    graph[now].sort()
    for i in graph[now]:
        if result[i] == 0:
            count += 1
            dfs(i)


dfs(r)
for j in range(1, n+1):
    print(result[j])
