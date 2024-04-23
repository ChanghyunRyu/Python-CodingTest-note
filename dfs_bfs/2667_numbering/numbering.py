import sys
from collections import deque

n = int(input())
building = []
result = []
for _ in range(n):
    line = list(map(int, sys.stdin.readline().rstrip()))
    building.append(line)


def dfs(a, b):
    building[a][b] = -1
    s = deque([(a, b)])
    count = 1
    while s:
        x, y = s.pop()
        if x-1 >= 0 and building[x-1][y] == 1:
            count += 1
            building[x-1][y] = -1
            s.append((x-1, y))
        if x+1 < n and building[x+1][y] == 1:
            count += 1
            building[x+1][y] = -1
            s.append((x+1, y))
        if y-1 >= 0 and building[x][y-1] == 1:
            count += 1
            building[x][y-1] = -1
            s.append((x, y-1))
        if y+1 < n and building[x][y+1] == 1:
            count += 1
            building[x][y+1] = -1
            s.append((x, y+1))
    return count


c = 0
for i in range(n):
    for j in range(n):
        if building[i][j] == 1:
            c += 1
            number = dfs(i, j)
            result.append(number)
result.sort()
print(c)
for num in result:
    print(num)
