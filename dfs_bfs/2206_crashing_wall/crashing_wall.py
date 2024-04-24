import sys
from collections import deque
INF = int(1e9)

n, m = map(int, input().split())
arr = []
guidance = [[[INF]*2 for _ in range(m)] for _ in range(n)]
guidance[0][0][0] = 1
for _ in range(n):
    line = list(map(int, sys.stdin.readline().rstrip()))
    arr.append(line)

q = deque([(0, 0, 0)])
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
while q:
    x, y, check = q.popleft()
    if x == n-1 and y == m-1:
        print(guidance[n-1][m-1][check])
        break
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if arr[nx][ny] == 1 and check == 0:
            guidance[nx][ny][1] = guidance[x][y][0]+1
            q.append((nx, ny, 1))
        if arr[nx][ny] == 0 and guidance[nx][ny][check] == INF:
            guidance[nx][ny][check] = guidance[x][y][check]+1
            if check == 0:
                guidance[nx][ny][1] = guidance[nx][ny][0]
            q.append((nx, ny, check))
if guidance[n-1][m-1][1] == INF and guidance[n-1][m-1][0] == INF:
    print(-1)
