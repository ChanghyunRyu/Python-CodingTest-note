from collections import deque


INF = int(1e9)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def solution(n, m, hole):
    treasure_map = [[0] * m for _ in range(n)]
    dp = [[[INF] * 2 for _ in range(m)] for _ in range(n)]
    for x, y in hole:
        treasure_map[x - 1][y - 1] = 1

    q = deque([(0, 0, 0)])
    dp[0][0][0] = 0
    dp[0][0][1] = 0
    while q:
        x, y, magic_shoes= q.popleft()
        if x == n - 1 and y == m - 1:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            check = 0 <= nx < n and 0 <= ny < m
            if check and dp[nx][ny][magic_shoes] == INF and treasure_map[nx][ny] == 0:
                dp[nx][ny][magic_shoes] = dp[x][y][magic_shoes] + 1
                q.append((nx, ny, magic_shoes))
            if not magic_shoes:
                nx = x + 2 * dx[i]
                ny = y + 2 * dy[i]
                check = 0 <= nx < n and 0 <= ny < m
                if check and dp[nx][ny][1] == INF and treasure_map[nx][ny] == 0:
                    dp[nx][ny][1] = dp[x][y][magic_shoes] + 1
                    q.append((nx, ny, 1))
    answer = min(dp[n - 1][m - 1])
    if answer == INF:
        return -1
    else:
        return answer
