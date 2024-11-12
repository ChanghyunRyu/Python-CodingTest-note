from collections import deque


T = int(input())
UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
left = {1: 0, 3: 0, 6: 0, 7: 0}
right ={1: 0, 3: 0, 4: 0, 5: 0}
up = {1:0, 2:0, 4: 0, 7: 0}
down = {1:0, 2:0, 5:0, 6:0}


for test_case in range(1, T + 1):
    n, m, r, c, l = map(int, input().split())
    tunnel = []
    for _ in range(n):
        tunnel.append(list(map(int, input().split())))
    answer = set()
    visited = [[False]*m for _ in range(n)]
    q = deque([(r, c, 1)])
    while q:
        x, y, count = q.popleft()
        visited[x][y] = True
        answer.add((x, y))
        if count == l:
            continue
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            check = 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]
            if not check:
                continue
            if i == UP and tunnel[x][y] in up and tunnel[nx][ny] in down:
                q.append((nx, ny, count+1))
            elif i == DOWN and tunnel[x][y] in down and tunnel[nx][ny] in up:
                q.append((nx, ny, count+1))
            elif i == LEFT and tunnel[x][y] in left and tunnel[nx][ny] in right:
                q.append((nx, ny, count+1))
            elif i == RIGHT and tunnel[x][y] in right and tunnel[nx][ny] in left:
                q.append((nx, ny, count+1))
    print('#{} {}'.format(test_case, len(answer)))
