dx = [1, 1, -1, -1]
dy = [1, -1, -1, 1]


def get_rectangle(x, y, direction, start, dessert, result):
    if cafes[x][y] in dessert:
        return
    dessert.add(cafes[x][y])
    if x == start[0] and y == start[1]:
        result.append(len(dessert))
        return
    visited[x][y] = True
    for i in range(2):
        direction = direction+i
        if direction > 3:
            continue
        nx = x+dx[direction]
        ny = y+dy[direction]
        check = 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]
        if check:
            get_rectangle(nx, ny, direction, start, set(dessert), result)
    visited[x][y] = False


T = int(input())
for test_case in range(1, T + 1):
    answer = -1
    N = int(input())
    cafes = []
    for _ in range(N):
        cafes.append(list(map(int, input().split())))
    visited = [[False]*N for _ in range(N)]
    r = []
    for i in range(N):
        for j in range(N):
            if i < N-1 and j < N-1:
                now = (i, j)
                get_rectangle(i+1, j+1, 0, now, set(), r)
    if r:
        answer = max(r)
    print('#{} {}'.format(test_case, answer))
