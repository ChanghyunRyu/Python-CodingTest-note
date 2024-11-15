dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def solution(command):
    direction = 0
    now = [0, 0]
    for c in command:
        if c == 'R':
            direction = (direction+1)%4
        elif c == 'L':
            direction = (direction-1)%4
        elif c == 'G':
            now[0] += dx[direction]
            now[1] += dy[direction]
        else:
            now[0] -= dx[direction]
            now[1] -= dy[direction]
    return now