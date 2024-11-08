## 미세먼지 안녕!

---

시간 제한: 1초, 메모리 제한: 512MB

미세먼지를 제거하기 위해 구사과는 공기청정기를 설치하려고 한다. 공기청정기의 성능을 테스트하기 위해 구사과는 집을 크기가 R×C인 격자판으로 나타냈고, 1×1 크기의 칸으로 나눴다. 
구사과는 뛰어난 코딩 실력을 이용해 각 칸 (r, c)에 있는 미세먼지의 양을 실시간으로 모니터링하는 시스템을 개발했다. 
(r, c)는 r행 c열을 의미한다.

공기청정기는 항상 1번 열에 설치되어 있고, 크기는 두 행을 차지한다. 
공기청정기가 설치되어 있지 않은 칸에는 미세먼지가 있고, (r, c)에 있는 미세먼지의 양은 Ar,c이다.

1초 동안 아래 적힌 일이 순서대로 일어난다.

1. 미세먼지가 확산된다. 확산은 미세먼지가 있는 모든 칸에서 동시에 일어난다.
- (r, c)에 있는 미세먼지는 인접한 네 방향으로 확산된다.
- 인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로는 확산이 일어나지 않는다.
- 확산되는 양은 Ar,c/5이고 소수점은 버린다. 즉, ⌊Ar,c/5⌋이다.
- (r, c)에 남은 미세먼지의 양은 Ar,c - ⌊Ar,c/5⌋×(확산된 방향의 개수) 이다.
2. 공기청정기가 작동한다.
- 공기청정기에서는 바람이 나온다.
- 위쪽 공기청정기의 바람은 반시계방향으로 순환하고, 아래쪽 공기청정기의 바람은 시계방향으로 순환한다.
- 바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동한다.
- 공기청정기에서 부는 바람은 미세먼지가 없는 바람이고, 공기청정기로 들어간 미세먼지는 모두 정화된다.

### 입력

- 첫째 줄에 R, C, T (6 ≤ R, C ≤ 50, 1 ≤ T ≤ 1,000) 가 주어진다.
- 둘째 줄부터 R개의 줄에 Ar,c (-1 ≤ Ar,c ≤ 1,000)가 주어진다. 공기청정기가 설치된 곳은 Ar,c가 -1이고, 나머지 값은 미세먼지의 양이다. 
- -1은 2번 위아래로 붙어져 있고, 가장 윗 행, 아랫 행과 두 칸이상 떨어져 있다.

### 출력

- 첫째 줄에 T초가 지난 후 구사과 방에 남아있는 미세먼지의 양을 출력한다.

---
### Problem Solved Check
- [x] 1회 24/11/08
- [ ] 2회
- [ ] 3회

~~~
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

~~~