from collections import deque

n, m, k = map(int, input().split())

passage = [[0]*m for _ in range(n)]
for _ in range(k):
    r, c = map(int, input().split())
    passage[r-1][c-1] = 1


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

answer = 0
for i in range(n):
    for j in range(m):
        if passage[i][j] == 1:
            q = deque([(i, j)])
            count = 0
            while q:
                x, y = q.popleft()
                if passage[x][y] == 0:
                    continue
                count += 1
                passage[x][y] = 0
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    check = 0 <= nx < n and 0 <= ny < m
                    if check and passage[nx][ny] == 1:
                        q.append((nx, ny))
            answer = max(answer, count)

print(answer)
