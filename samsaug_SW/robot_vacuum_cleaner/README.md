## 로봇 청소기

---

시간 제한: 2초, 메모리 제한: 512MB

로봇 청소기와 방의 상태가 주어졌을 때, 청소하는 영역의 개수를 구하는 프로그램을 작성하시오.

로봇 청소기가 있는 방은 N x M 크기의 직사각형으로 나타낼 수 있으며, 1 x 1 기의 정사각형 칸으로 나누어져 있다. 
각각의 칸은 벽 또는 빈 칸이다. 청소기는 바라보는 방향이 있으며, 이 방향은 동, 서, 남, 북 중 하나이다.

장 북쪽 줄의 가장 서쪽 칸의 좌표가 (0, 0), 가장 남쪽 줄의 가장 동쪽 칸의 좌표가 (N-1, M-1)이다.

로봇 청소기는 다음과 같이 작동한다.

1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
2. 현재 칸의 주변  4칸 중 청소되지 않은 빈 칸이 없는 경우,
   1. 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
   2. 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
   1. 반시계 방향으로 90도 회전한다.
   2. 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
   3. 1번으로 돌아간다.

### 입력

- 첫째 줄에 방의 크기 N과 M이 입력된다 (3 ≤ N, M ≤ 50) 
- 둘째 줄에 처음에 로봇 청소기가 있는 칸의 좌표 (r, c)와 처음에 로봇 청소기가 바라보는 방향 d가 입력된다.
- d가 0인 경우 북쪽, 1인 경우 동쪽, 2인 경우 남쪽, 3인 경우 서쪽을 바라보고 있는 것이다.
- 셋째 줄부터 N개의 줄에 각 장소의 상태를 나타내는 N x M 개의 값이 한 줄에 M개씩 입력된다.
- 값이 0인 경우 청소되지 않은 빈 칸, 1인 경우 벽이 있는 것이다. 
- 방의 가장 북쪽, 가장 남쪽, 가장 서쪽, 가장 동쪽 줄 중 하나 이상에 위치한 모든 칸에는 벽이 있다. 로봇 청소기가 있는 칸은 항상 빈 칸이다.

### 출력

- 로봇 청소기가 작동을 시작한 후 작동을 멈출 때까지 청소하는 칸의 개수를 출력한다.

---
### Problem Solved Check
- [x] 1회 24/10/23
- [ ] 2회
- [ ] 3회

진행 방향을 유지하는 것이 아니라, 90도 회전부터하고 탐색하는 것. 문제를 정확히 읽지 않아 한 번 틀렸다.
~~~
import sys


n, m = map(int, input().split())
robot = list(map(int, input().split()))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

room = []
for _ in range(n):
    room.append(list(map(int, sys.stdin.readline().split())))


def dfs(x, y, direction, count, room_map):
    if room_map[x][y] == 0:
        count += 1
        room_map[x][y] = 2
    for i in range(4):
        direction = (direction - 1) % 4
        nx, ny = x+dx[direction], y+dy[direction]
        check = 0 <= nx < len(room_map) and 0 <= ny < len(room_map[0])
        if check and room_map[nx][ny] == 0:
            return dfs(nx, ny, direction, count, room_map)

    bx, by = x-dx[direction], y-dy[direction]
    check = 0 <= bx < len(room_map) and 0 <= by < len(room_map[0])
    if check and room[bx][by] == 1:
        return count
    else:
        return dfs(bx, by, direction, count, room_map)


answer = dfs(robot[0], robot[1], robot[2], 0, room)
print(answer)

~~~