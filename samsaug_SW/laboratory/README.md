## 연구소

---

시간 제한: 2초, 메모리 제한: 512MB

인체에 치명적인 바이러스를 연구하던 연구소에서 바이러스가 유출되었다. 
다행히 바이러스는 아직 퍼지지 않았고, 바이러스의 확산을 막기 위해서 연구소에 벽을 세우려고 한다.

연구소는 크기가 N×M인 직사각형으로 나타낼 수 있으며, 직사각형은 1×1 크기의 정사각형으로 나누어져 있다. 
연구소는 빈 칸, 벽으로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다. 

벽을 3개 세운 뒤, 바이러스가 퍼질 수 없는 곳을 안전 영역이라고 한다. 

연구소의 지도가 주어졌을 때 얻을 수 있는 안전 영역 크기의 최댓값을 구하는 프로그램을 작성하시오.

### 입력

- 첫째 줄에 지도의 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 8)
- 둘째 줄부터 N개의 줄에 지도의 모양이 주어진다. 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 위치이다. 2의 개수는 2보다 크거나 같고, 10보다 작거나 같은 자연수이다.
- 빈 칸의 개수는 3개 이상이다.

### 출력

- 첫째 줄에 얻을 수 있는 안전 영역의 최대 크기를 출력한다.

---
### Problem Solved Check
- [x] 1회 24/10/23
- [ ] 2회
- [ ] 3회

simple is best 방법으로 풀었는데, 더 좋은 방법이 있는지는 확인을 해봐야할 것 같다.
~~~
from itertools import combinations
import copy


def spread_virus(laboratory):
    for i in range(len(laboratory)):
        for j in range(len(laboratory[i])):
            if laboratory[i][j] == 2:
                dfs(i, j, laboratory)

    result = 0
    for i in range(len(laboratory)):
        for j in range(len(laboratory[i])):
            if laboratory[i][j] == 0:
                result += 1
    return result


def dfs(x, y, laboratory):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        check = 0 <= nx < len(laboratory) and 0 <= ny < len(laboratory[0])
        if not check or laboratory[nx][ny] != 0:
            continue
        laboratory[nx][ny] = 2
        dfs(nx, ny, laboratory)


n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

points = [(i, j) for i in range(n) for j in range(m)]

answer = 0
for com in combinations(points, 3):
    new_board = copy.deepcopy(board)
    flag = True
    for x, y in com:
        if new_board[x][y] == 1 or new_board[x][y] == 2:
            flag = False
            break
        else:
            new_board[x][y] = 1
    if flag:
        answer = max(answer, spread_virus(new_board))
print(answer)

~~~