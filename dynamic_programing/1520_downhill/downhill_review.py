n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
dp = [[-1]*m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):
    if x == n-1 and y == m-1:
        return 1

    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        check = 0 <= nx < n and 0 <= ny < m
        if check and arr[x][y] > arr[nx][ny]:
            dp[x][y] += dfs(nx, ny)

    return dp[x][y]


print(dfs(0, 0))
