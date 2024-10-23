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
