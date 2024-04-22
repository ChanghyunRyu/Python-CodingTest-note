import sys
from collections import deque

n, m = map(int, input().split())
field = []
for _ in range(m):
    tomatoes = list(map(int , sys.stdin.readline().split()))
    field.append(tomatoes)

q = deque([])
count = 0
check = True
for i in range(n):
    for j in range(m):
        if field[j][i] == 1:
            q.append((i, j, 0))

while q:
    x, y, c = q.popleft()
    if count < c:
        count = c
    if x+1 < n and field[y][x+1] == 0:
        field[y][x+1] = 1
        q.append((x+1, y, c+1))
    if x-1 >= 0 and field[y][x-1] == 0:
        field[y][x-1] = 1
        q.append((x-1, y, c+1))
    if y+1 < m and field[y+1][x] == 0:
        field[y+1][x] = 1
        q.append((x, y+1, c+1))
    if y-1 >= 0 and field[y-1][x] == 0:
        field[y-1][x] = 1
        q.append((x, y-1, c+1))
for row in field:
    for tomato in row:
        if tomato == 0:
            check = False
            break

if not check:
    print(-1)
else:
    print(count)
