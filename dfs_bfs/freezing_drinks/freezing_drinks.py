n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(input())

graph = []
for a in arr:
    tmp = []
    for b in a:
        tmp.append(int(b))
    graph.append(tmp)


def dfs(i, j):
    global result
    if i < 0 or i >= n or j < 0 or j >= m:
        return False
    if graph[i][j] == 0:
        graph[i][j] = 1
        dfs(i-1, j)
        dfs(i, j-1)
        dfs(i+1, j)
        dfs(i, j+1)
        return True
    return False


result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1
print(result)
