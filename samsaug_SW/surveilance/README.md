## 감시

---

시간 제한: 1초, 메모리 제한: 512MB

스타트링크의 사무실은 1×1크기의 정사각형으로 나누어져 있는 N×M 크기의 직사각형으로 나타낼 수 있다. 
사무실에는 총 K개의 CCTV가 설치되어져 있는데, CCTV는 5가지 종류가 있다. 각 CCTV가 감시할 수 있는 방법은 다음과 같다.

1번 CCTV는 한 쪽 방향만 감시할 수 있다. 
2번과 3번은 두 방향을 감시할 수 있는데, 2번은 감시하는 방향이 서로 반대방향이어야 하고, 
3번은 직각 방향이어야 한다. 4번은 세 방향, 5번은 네 방향을 감시할 수 있다.

CCTV는 감시할 수 있는 방향에 있는 칸 전체를 감시할 수 있다. 사무실에는 벽이 있는데, CCTV는 벽을 통과할 수 없다. 
CCTV가 감시할 수 없는 영역은 사각지대라고 한다.

CCTV는 회전시킬 수 있는데, 회전은 항상 90도 방향으로 해야 하며, 
감시하려고 하는 방향이 가로 또는 세로 방향이어야 한다.

CCTV는 CCTV를 통과할 수 있다.
사무실의 크기와 상태, 그리고 CCTV의 정보가 주어졌을 때, 
CCTV의 방향을 적절히 정해서, 사각 지대의 최소 크기를 구하는 프로그램을 작성하시오.

### 입력

- 첫째 줄에 사무실의 세로 크기 N과 가로 크기 M이 주어진다. (1 ≤ N, M ≤ 8)
- 둘째 줄부터 N개의 줄에는 사무실 각 칸의 정보가 주어진다. 0은 빈 칸, 6은 벽, 1~5는 CCTV를 나타내고, 문제에서 설명한 CCTV의 종류이다. 
- CCTV의 최대 개수는 8개를 넘지 않는다.

### 출력

- 첫째 줄에 사각 지대의 최소 크기를 출력한다.

---
### Problem Solved Check
- [x] 1회 24/10/25 
- [ ] 2회
- [ ] 3회
~~~
import copy


n, m = map(int, input().split())
room = []
for _ in range(n):
    room.append(list(map(int, input().split())))

cctv = []
for i in range(n):
    for j in range(m):
        if room[i][j] != 6 and room[i][j] != 0:
            cctv.append((room[i][j], i, j))


def dfs(room_map, cctvs, idx, answer):
    if idx >= len(cctvs):
        temp = 0
        for i in range(len(room_map)):
            for j in range(len(room_map[0])):
                if room_map[i][j] == 0:
                    temp += 1
        answer.append(temp)
        return
    number, x, y = cctvs[idx]
    direction = set_dxy(number)
    for dxy in direction:
        new_map = copy.deepcopy(room_map)
        for dx, dy in dxy:
            nx = x+dx
            ny = y+dy
            while 0 <= nx < len(new_map) and 0 <= ny < len(new_map[0]) and new_map[nx][ny] != 6:
                if new_map[nx][ny] == 0:
                    new_map[nx][ny] = 7
                nx = nx+dx
                ny = ny+dy
        dfs(new_map, cctvs, idx+1, answer)


def set_dxy(number):
    if number == 1:
        return [[[1, 0]], [[-1, 0]], [[0, 1]], [[0, -1]]]
    elif number == 2:
        return [[[1, 0], [-1, 0]], [[0, 1], [0, -1]]]
    elif number == 3:
        return [[[-1, 0], [0, 1]], [[0, 1], [1, 0]], [[1, 0], [0, -1]], [[0, -1], [-1, 0]]]
    elif number == 4:
        return [[[0, -1], [-1, 0], [0, 1]], [[-1, 0], [0, 1], [1, 0]], [[0, 1], [1, 0], [0, -1]], [[1, 0], [0, -1], [-1, 0]]]
    elif number == 5:
        return [[[1, 0], [-1, 0], [0, 1], [0, -1]]]


result = []
dfs(room, cctv, 0, result)
print(min(result))

~~~
