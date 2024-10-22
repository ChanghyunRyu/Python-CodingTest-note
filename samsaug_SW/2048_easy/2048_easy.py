import copy


def move_board(command, board_map):
    if command == 'UP':
        for y in range(n):
            temp = []
            flag = True
            for x in range(n):
                if board_map[x][y] == 0:
                    continue
                if not temp or not flag or temp[-1] != board_map[x][y]:
                    flag = True
                    temp.append(board_map[x][y])
                elif flag and temp[-1] == board_map[x][y]:
                    temp[-1] += board_map[x][y]
                    flag = False

            for i in range(n):
                if i >= len(temp):
                    board_map[i][y] = 0
                else:
                    board_map[i][y] = temp[i]
    elif command == 'DOWN':
        for y in range(n):
            temp = []
            flag = True
            for x in range(n-1, -1, -1):
                if board_map[x][y] == 0:
                    continue
                if not temp or not flag or temp[-1] != board_map[x][y]:
                    flag = True
                    temp.append(board_map[x][y])
                elif flag and temp[-1] == board_map[x][y]:
                    temp[-1] += board_map[x][y]
                    flag = False

            for i in range(n):
                if i >= len(temp):
                    board_map[n-i-1][y] = 0
                else:
                    board_map[n-i-1][y] = temp[i]
    elif command == 'LEFT':
        for x in range(n):
            temp = []
            flag = True
            for y in range(n):
                if board_map[x][y] == 0:
                    continue
                if not temp or not flag or temp[-1] != board_map[x][y]:
                    flag = True
                    temp.append(board_map[x][y])
                elif flag and temp[-1] == board_map[x][y]:
                    flag = False
                    temp[-1] += board_map[x][y]

            for i in range(n):
                if i >= len(temp):
                    board_map[x][i] = 0
                else:
                    board_map[x][i] = temp[i]
    else:
        for x in range(n):
            temp = []
            flag = True
            for y in range(n-1, -1, -1):
                if board_map[x][y] == 0:
                    continue
                if not temp or not flag or temp[-1] != board_map[x][y]:
                    flag = True
                    temp.append(board_map[x][y])
                elif flag and temp[-1] == board_map[x][y]:
                    flag = False
                    temp[-1] += board_map[x][y]

            for i in range(n):
                if i >= len(temp):
                    board_map[x][n-i-1] = 0
                else:
                    board_map[x][n-i-1] = temp[i]


def dfs(command, board_map, count, answer):
    move_board(command, board_map)
    if count == 5:
        answer.append(max(map(max, board_map)))
        return
    dfs('UP', copy.deepcopy(board_map), count + 1, answer)
    dfs('DOWN', copy.deepcopy(board_map), count + 1, answer)
    dfs('LEFT', copy.deepcopy(board_map), count + 1, answer)
    dfs('RIGHT', copy.deepcopy(board_map), count + 1, answer)


n = int(input())
board = [0*n for _ in range(n)]
for i in range(n):
    board[i] = list(map(int, input().split()))

result = []
dfs('UP', copy.deepcopy(board), 1, result)
dfs('DOWN', copy.deepcopy(board), 1, result)
dfs('LEFT', copy.deepcopy(board), 1, result)
dfs('RIGHT', copy.deepcopy(board), 1, result)
print(max(result))
