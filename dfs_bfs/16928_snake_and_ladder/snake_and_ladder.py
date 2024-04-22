import sys
from collections import deque
INF = int(1e9)

n, m = map(int, input().split())
ladder = {}
snake = {}
for _ in range(n):
    start, end = map(int, sys.stdin.readline().split())
    ladder[start] = end
for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    snake[start] = end

board = [INF]*101
board[1] = 0
q = deque([1])
while q:
    now = q.popleft()
    if now == 100:
        print(board[now])
        break
    if now in ladder.keys():
        next = ladder[now]
        if board[next] > board[now]:
            board[next] = board[now]
            q.append(next)
    elif now in snake.keys():
        next = snake[now]
        if board[next] > board[now]:
            board[next] = board[now]
            q.append(next)
    else:
        for i in range(1, 7):
            next = now + i
            if next < 101 and board[next] > board[now] + 1:
                board[next] = board[now] + 1
                q.append(next)
