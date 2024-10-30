## 드래곤 커브

---

시간 제한: 1초, 메모리 제한: 512MB
드래곤 커브는 다음과 같은 세 가지 속성으로 이루어져 있으며, 이차원 좌표 평면 위에서 정의된다. 
좌표 평면의 x축은 → 방향, y축은 ↓ 방향이다.

1. 시작점
2. 시작 방향
3. 세대

K(K > 1)세대 드래곤 커브는 K-1세대 드래곤 커브를 끝 점을 기준으로 90도 시계 방향 회전 시킨 다음, 그것을 끝 점에 붙인 것이다.
크기가 100×100인 격자 위에 드래곤 커브가 N개 있다. 이때, 크기가 1×1인 정사각형의 
네 꼭짓점이 모두 드래곤 커브의 일부인 정사각형의 개수를 구하는 프로그램을 작성하시오. 
격자의 좌표는 (x, y)로 나타내며, 0 ≤ x ≤ 100, 0 ≤ y ≤ 100만 유효한 좌표이다.

### 입력

- 첫째 줄에 드래곤 커브의 개수 N(1 ≤ N ≤ 20)이 주어진다. 
- 둘째 줄부터 N개의 줄에는 드래곤 커브의 정보가 주어진다. 
- 드래곤 커브의 정보는 네 정수 x, y, d, g로 이루어져 있다.
- x와 y는 드래곤 커브의 시작 점, d는 시작 방향, g는 세대이다. (0 ≤ x, y ≤ 100, 0 ≤ d ≤ 3, 0 ≤ g ≤ 10)
- 입력으로 주어지는 드래곤 커브는 격자 밖으로 벗어나지 않는다. 드래곤 커브는 서로 겹칠 수 있다.
- 방향은 0, 1, 2, 3 중 하나이고, 다음을 의미한다.
  - 0: x좌표가 증가하는 방향 (→)
  - 1: y좌표가 감소하는 방향 (↑)
  - 2: x좌표가 감소하는 방향 (←)
  - 3: y좌표가 증가하는 방향 (↓)

### 출력

- 첫째 줄에 크기가 1×1인 정사각형의 네 꼭짓점이 모두 드래곤 커브의 일부인 것의 개수를 출력한다.

---
### Problem Solved Check
- [x] 1회 24/10/30
- [ ] 2회
- [ ] 3회

매 세대마다 끝점은 마지막에 초기화 하는 부분, (x, y) 좌표를 입력하는 반대로하는 실수를 하여 오래 걸림.
~~~
n = int(input())
curves = []
for _ in range(n):
    curves.append(list(map(int, input().split())))

direction = [
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1),
    (-1, -1),
    (-1, 0),
    (-1, 1)
]
d_idx = dict()
for idx in range(len(direction)):
    d_idx[direction[idx]] = idx
board = [[0]*101 for _ in range(101)]


def draw_dragon_curve(x, y, d, g, arr):
    # 시작점 등록
    start = (x, y)
    arr[x][y] = 1
    dxy = [[0, 1], [-1, 0], [0, -1], [1, 0]]
    points = set()
    points.add(start)
    end = start
    for i in range(g+1):
        if i == 0:
            end = (start[0]+dxy[d][0], start[1]+dxy[d][1])
            arr[end[0]][end[1]] = 1
            points.add(end)
            continue
        new_points = set(points)
        for point in points:
            if end == point:
                continue
            # 끝점 기준 90도 틀어진 점 구하기
            # 방향 구하기
            dx = point[0] - end[0]
            dy = point[1] - end[1]
            dx_size = abs(dx)
            dy_size = abs(dy)
            if dx_size == 0:
                dx = 0
            else:
                dx = dx//dx_size
            if dy_size == 0:
                dy = 0
            else:
                dy = dy//dy_size
            temp = (dx, dy)
            temp_idx = (d_idx[temp]+2) % 8
            new_dxy = direction[temp_idx]

            # 90도 틀어진 방향의 점 계산
            new_point = (end[0]+(new_dxy[0]*dy_size), end[1]+(new_dxy[1]*dx_size))
            new_points.add(new_point)
            arr[new_point[0]][new_point[1]] = 1
            if point == start:
                temp_end = new_point
        end = temp_end
        points = new_points


for curve in curves:
    draw_dragon_curve(curve[1], curve[0], curve[2], curve[3], board)

answer = 0
for i in range(100):
    for j in range(100):
        if board[i][j] == 1 and board[i+1][j] == 1 and board[i][j+1] == 1 and board[i+1][j+1] == 1:
            answer += 1
print(answer)

~~~
