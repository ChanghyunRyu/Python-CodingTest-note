import sys
from collections import deque

n, m, h = map(int, input().split())
field = []
for _ in range(h):
    temp = []
    for _ in range(m):
        row = list(map(int, sys.stdin.readline().split()))
        temp.append(row)
    field.append(temp)

q = deque([])
count = 0
for k in range(h):
    for j in range(m):
        for i in range(n):
            if field[k][j][i] == 1:
                q.append((i, j, k, 0))

while q:
    x, y, z, c = q.popleft()
    if c > count:
        count = c
    if z+1 < h and field[z+1][y][x] == 0:
        field[z+1][y][x] = 1
        q.append((x, y, z+1, c+1))
    if z-1 >= 0 and field[z-1][y][x] == 0:
        field[z-1][y][x] = 1
        q.append((x, y, z-1, c+1))
    if y+1 < m and field[z][y+1][x] == 0:
        field[z][y+1][x] = 1
        q.append((x, y+1, z, c+1))
    if y-1 >= 0 and field[z][y-1][x] == 0:
        field[z][y-1][x] = 1
        q.append((x, y-1, z, c+1))
    if x+1 < n and field[z][y][x+1] == 0:
        field[z][y][x+1] = 1
        q.append((x+1, y, z, c+1))
    if x-1 >= 0 and field[z][y][x-1] == 0:
        field[z][y][x-1] = 1
        q.append((x-1, y, z, c+1))

check = True
for f in field:
    for row in f:
        for tomato in row:
            if tomato == 0:
                check = False
                break

if not check:
    print(-1)
else:
    print(count)
