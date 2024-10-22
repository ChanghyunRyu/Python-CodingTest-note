def roll_dice(command, d):
    if command == 1:
        dice['top'], dice['right'], dice['left'], dice['bottom'] = dice['left'], dice['top'], dice['bottom'], dice['right']
    elif command == 2:
        dice['top'], dice['right'], dice['left'], dice['bottom'] = dice['right'], dice['bottom'], dice['top'], dice['left']
    elif command == 3:
        dice['top'], dice['down'], dice['bottom'], dice['up'] = dice['down'], dice['bottom'], dice['up'], dice['top']
    else:
        dice['top'], dice['down'], dice['bottom'], dice['up'] = dice['up'], dice['top'], dice['down'], dice['bottom']


n, m, x, y, k = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

commands = list(map(int, input().split()))
dice = {'top': 0, 'bottom': 0, 'up': 0, 'down': 0, 'left': 0, 'right': 0}

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

result = []
for c in commands:
    nx = x+dx[c-1]
    ny = y+dy[c-1]
    check_range = 0 <= nx < n and 0 <= ny < m
    if not check_range:
        continue
    roll_dice(c, dice)
    result.append(dice['top'])
    if board[nx][ny] == 0:
        board[nx][ny] = dice['bottom']
    else:
        dice['bottom'] = board[nx][ny]
        board[nx][ny] = 0
    x, y = nx, ny

for r in result:
    print(r)
