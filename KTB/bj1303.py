from collections import deque


n, m = map(int, input().split())
war = []
for _ in range(m):
    war.append(list(input()))
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = {"W": 0, "B": 0}


for i in range(m):
    for j in range(n):
        if war[i][j] == "W" or war[i][j] == "B":
            count = set()
            color = war[i][j]
            q = deque([(i, j)])
            while q:
                x, y = q.popleft()
                count.add((x, y))
                war[x][y] = 'O'
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    check = 0 <= nx < m and 0 <= ny < n
                    if check and war[nx][ny] == color:
                        q.append((nx, ny))
            answer[color] += len(count)**2


print('{} {}'.format(answer['W'], answer['B']))
