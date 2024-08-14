from collections import deque
INF = int(1e8)


def solution(board):
    n = len(board)
    dp = [[INF]*n for _ in range(n)]
    answer = [get_result(0, board), get_result(1, board)]
    return min(answer)


def get_result(direction, board):
    q = deque([(0, (0, 0), direction)])
    n = len(board)
    dp = [[INF] * n for _ in range(n)]
    while q:
        price, point, direction = q.popleft()
        if dp[point[0]][point[1]] + 500 <= price:
            continue
        dp[point[0]][point[1]] = min(price, dp[point[0]][point[1]])
        dx = [0, 1, -1, 0]
        dy = [1, 0, 0, -1]
        for i in range(4):
            nx = point[0] + dx[i]
            ny = point[1] + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if board[nx][ny] == 1:
                continue
            new_price = price + (100 if direction == i else 600)
            if dp[nx][ny] >= new_price:
                q.append((new_price, (nx, ny), i))
    return dp[n-1][n-1]


print(solution([[0,0,0,0,0,0,0,1],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,1,0,0],
                [0,0,0,0,1,0,0,0],
                [0,0,0,1,0,0,0,1],
                [0,0,1,0,0,0,1,0],
                [0,1,0,0,0,1,0,0],
                [1,0,0,0,0,0,0,0]]))
print(solution([[0,0,0,0,0,0,0,0,0,1],
[0,1,1,1,1,1,1,1,0,1],
[0,1,1,1,1,1,1,1,0,1],
[0,1,1,1,1,1,1,0,0,1],
[0,1,1,1,1,1,1,0,1,1],
[0,1,1,1,1,1,1,0,1,1],
[0,1,1,1,1,0,0,0,0,0],
[0,1,1,1,1,0,1,1,1,0],
[0,0,0,0,0,0,1,1,1,0],
[1,1,1,1,1,1,1,1,1,0]]))

