import sys


r, c, t = map(int, sys.stdin.readline().split())
home = []
for _ in range(r):
    home.append(list(map(int, sys.stdin.readline().split())))
air_purifier = []
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def diffusion():
    new_home = [[0]*c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            if len(air_purifier) < 3 and home[x][y] == -1:
                new_home[x][y] = -1
                air_purifier.append((x, y))
                continue
            elif home[x][y] < 5:
                new_home[x][y] += home[x][y]
                continue

            amount = home[x][y] // 5
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                check = 0 <= nx < r and 0 <= ny < c
                if check and home[nx][ny] != -1:
                    new_home[nx][ny] += amount
                    home[x][y] -= amount
            new_home[x][y] += home[x][y]
    return new_home


def air_purification(x, y, dust, direction, d_i):
    if (x, y) in air_purifier:
        return
    new_dust = home[x][y]
    home[x][y] = dust
    nx = x+direction[d_i][0]
    ny = y+direction[d_i][1]
    check = 0 <= nx < r and 0 <= ny < c
    if check:
        air_purification(nx, ny, new_dust, direction, d_i)
    else:
        d_i += 1
        nx = x + direction[d_i][0]
        ny = y + direction[d_i][1]
        air_purification(nx, ny, new_dust, direction, d_i)


dxy1 = [[0, 1], [-1, 0], [0, -1], [1, 0]]
dxy2 = [[0, 1], [1, 0], [0, -1], [-1, 0]]
for _ in range(t):
    home = diffusion()
    air_purification(air_purifier[0][0], air_purifier[0][1] + 1, 0, dxy1, 0)
    air_purification(air_purifier[1][0], air_purifier[1][1] + 1, 0, dxy2, 0)
print(sum(list(map(sum, home)))+2)
