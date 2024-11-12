from collections import defaultdict

T = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def reverse_direction(direction):
    if direction == 1:
        return 2
    elif direction == 2:
        return 2
    elif direction == 3:
        return 4
    else:
        return 3


def get_next_point(n, x, y, direction, size):
    nx = x + dx[direction-1]
    ny = y + dy[direction-1]
    if nx == 0 or nx == n - 1 or ny == 0 or ny == n - 1:
        direction = reverse_direction(direction)
        size = size // 2
    return nx, ny, size, direction


def move_micro(micros, n):
    temp = defaultdict(list)
    for key in micros:
        x, y = key[0], key[1]
        size, direction = micros[key]
        x, y, size, direction = get_next_point(n, x, y, direction, size)
        temp[(x, y)].append((size, direction))
    new_micro = {}
    for key in temp:
        d = 0
        max_size = 0
        new_size = 0
        for size, direction in temp[key]:
            new_size += size
            if max_size < size:
                d = direction
                max_size = size
        new_micro[key] = (new_size, d)
    return new_micro


for test_case in range(1, T + 1):
    answer = 0
    n, m, k = map(int, input().split())
    micro = {}
    for _ in range(k):
        x, y, size, direction = map(int, input().split())
        micro[(x, y)] = (size, direction)
    for _ in range(m):
        micro = move_micro(micro, n)
    for key in micro:
        answer += micro[key][0]
    print('#{} {}'.format(test_case, answer))
