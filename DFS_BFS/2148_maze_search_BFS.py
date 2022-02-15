# 백준 문제 2148번
from collections import deque
n, m = map(int, input().split())
maze = []
for i in range(n):
    maze.append(list(map(int, input())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def maze_bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))
    return maze[n-1][m-1]


print(maze_bfs(0, 0))
for i in range(n):
    print()
    for j in range(m):
        print("%3d" % maze[i][j], end=' ')
