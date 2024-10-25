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
