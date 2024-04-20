import sys
from collections import deque
INF = int(1e9)

T = int(input())
result = []
for _ in range(T):
    l = int(sys.stdin.readline().rstrip())
    start = list(map(int, sys.stdin.readline().rstrip().split()))
    end = list(map(int, sys.stdin.readline().rstrip().split()))
    q = deque([start])
    board = [[INF]*l for _ in range(l)]
    board[start[0]][start[1]] = 0
    while q:
        x, y = q.popleft()
        if x == end[0] and y == end[1]:
            result.append(board[x][y])
            break
        if x+2 < l and y-1 >= 0 and board[x+2][y-1] > board[x][y]+1:
            board[x+2][y-1] = board[x][y]+1
            q.append((x+2, y-1))
        if x+2 < l and y+1 < l and board[x+2][y+1] > board[x][y]+1:
            board[x+2][y+1] = board[x][y]+1
            q.append((x+2, y+1))
        if x+1 < l and y-2 >= 0 and board[x+1][y-2] > board[x][y]+1:
            board[x+1][y-2] = board[x][y]+1
            q.append((x+1, y-2))
        if x+1 < l and y+2 < l and board[x+1][y+2] > board[x][y]+1:
            board[x+1][y+2] = board[x][y]+1
            q.append((x+1, y+2))
        if x-1 >= 0 and y+2 < l and board[x-1][y+2] > board[x][y]+1:
            board[x-1][y+2] = board[x][y]+1
            q.append((x-1, y+2))
        if x-2 >= 0 and y+1 < l and board[x-2][y+1] > board[x][y]+1:
            board[x-2][y+1] = board[x][y]+1
            q.append((x-2, y+1))
        if x-1 >= 0 and y-2 >= 0 and board[x-1][y-2] > board[x][y]+1:
            board[x-1][y-2] = board[x][y]+1
            q.append((x-1, y-2))
        if x-2 >= 0 and y-1 >= 0 and board[x-2][y-1] > board[x][y]+1:
            board[x-2][y-1] = board[x][y]+1
            q.append((x-2, y-1))

for r in result:
    print(r)
