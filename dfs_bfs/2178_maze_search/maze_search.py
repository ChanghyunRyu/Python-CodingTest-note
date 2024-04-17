import sys
from collections import deque

n, m = map(int, input().split())
maze = []
for _ in range(n):
    row = list(map(int, sys.stdin.readline().rstrip()))
    maze.append(row)
visited = [[False]*(m) for _ in range(n)]
q = deque([(0, 0, 1)])
result = 0

while q:
    x, y, count = q.popleft()
    if x == n-1 and y == m-1:
        result = count
        break
    if x-1 >= 0 and not visited[x-1][y] and maze[x-1][y] == 1:
        visited[x-1][y] = True
        q.append((x-1, y, count+1))
    if x+1 < n and not visited[x+1][y] and maze[x+1][y] == 1:
        visited[x+1][y] = True
        q.append((x+1, y, count+1))
    if y-1 >= 0 and not visited[x][y-1] and maze[x][y-1] == 1:
        visited[x][y-1] = True
        q.append((x, y-1, count+1))
    if y+1 < m and not visited[x][y+1] and maze[x][y+1] == 1:
        visited[x][y+1] = True
        q.append((x, y+1, count+1))

print(result)
