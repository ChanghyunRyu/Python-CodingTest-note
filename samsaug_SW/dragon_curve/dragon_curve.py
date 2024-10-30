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
