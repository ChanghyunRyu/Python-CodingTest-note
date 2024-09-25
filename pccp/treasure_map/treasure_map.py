from collections import deque


def solution(n, m, hole):
    mp = [[0]*m for _ in range(n)]
    for x, y in hole:
        mp[x-1][y-1] = 1
    visited = [[[-1, -1] for _ in range(m)] for _ in range(n)]
    q = deque()
    q.append((0, 0, 0))
    visited[0][0][0] = 0
    direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    while q:
        x, y, j = q.popleft()
        if mp[x][y] == 1:
            continue
        for dx, dy in direction:
            nx = x+dx
            ny = y+dy
            outside = nx < 0 or ny < 0 or nx > n-1 or ny > m-1
            if outside or mp[nx][ny] > 0 or visited[nx][ny][j] != -1:
                continue
            q.append((nx, ny, j))
            visited[nx][ny][j] = visited[x][y][j] + 1
        if j:
            continue
        for dx, dy in direction:
            nx = x+dx*2
            ny = y+dy*2
            outside = nx < 0 or ny < 0 or nx > n-1 or ny > m-1
            if outside or mp[nx][ny] > 0 or visited[nx][ny][j+1] != -1:
                continue
            q.append((nx, ny, j+1))
            visited[nx][ny][j+1] = visited[x][y][j] + 1
    answer = visited[n-1][m-1][1]
    if 0 <= visited[n-1][m-1][0] < visited[n-1][m-1][1]:
        answer = visited[n-1][m-1][0]
    return answer


print(solution(4, 4, [[2, 3], [3, 3]]))
print(solution(5, 4, [[1, 4], [2, 1], [2, 2], [2, 3], [2, 4], [3, 3], [4, 1], [4, 3], [5, 3]]))
print(solution(3, 3, [[1, 3], [2, 3], [3, 1], [3, 2]]))
