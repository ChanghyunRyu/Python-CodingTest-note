import sys
import heapq


tetris=[[(0, 0), (0, 1), (0, 2), (0, 3)],\
        [(0, 0), (1, 0), (2, 0), (3, 0)],\
        [(0, 0), (1, 0), (0, 1), (1, 1)],\
        [(0, 0), (1, 0), (2, 0), (2, 1)],\
        [(0, 0), (1, 0), (2, 0), (2, -1)],\
        [(0, 0), (0, 1), (1, 1), (2, 1)],\
        [(0, 0), (0, 1), (1, 0),(2, 0)],\
        [(0, 0), (1, 0), (1, 1), (1, 2)],\
        [(0, 0), (1, -1), (1, 0), (1, -2)],\
        [(0,0),(0,1),(0,2),(1,2)],\
        [(0,0),(1,0),(0,1),(0,2)],\
        [(0,0),(1,0),(1,1),(2,1)],\
        [(0,0),(1,0),(1,-1),(2,-1)],\
        [(0,0),(0,1),(-1,1),(-1,2)],\
        [(0,0),(0,1),(1,1),(1,2)],\
        [(0,0),(1,-1),(1,0),(1,1)],\
        [(0,0),(0,1),(0,2),(1,1)],\
        [(0,0),(1,0),(1,1),(2,0)],\
        [(0,0),(1,0),(1,-1),(2,0)]]


def search_tet(x, y, board_map):
    result = 0
    for tet in tetris:
        temp = 0
        flag = False
        for i in range(4):
            nx = x+tet[i][0]
            ny = y+tet[i][1]
            check = 0 <= nx < len(board_map) and 0 <= ny < len(board_map[0])
            if not check:
                flag = True
                break
            temp += board_map[nx][ny]
        if flag:
            continue
        result = max(result, temp)
    return result


n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))

answer = 0
for i in range(n):
    for j in range(m):
        answer = max(answer, search_tet(i, j, board))
print(answer)
