# 아이디어 자체는 괜찮았으나 꼬리의 방향을 정하는 것이 잘못되었다.
# 처음 아이디어: 주변에서 뱀 숫자(2)를 찾아서 진행했는데 이럴 경우
# 0 2 2
# 0 2 2 이렇게 지그재그로 지나가는 경우는 잘못된 꼬리 위치를 찾을 가능성이 있다.
# 따라서 각 좌표의 방향을 기록하는 형식으로 문제를 해결했다.
# 방향을 정하는 등의 다른 설계는 괜찮았으나 소모되는 시간이 오래 걸렸다.
import sys

n = int(input())
game_table = [[0]*n for i in range(n)]
k = int(input())
for i in range(k):
    x, y = map(int, sys.stdin.readline().split())
    game_table[x-1][y-1] = 1

l = int(input())
time_table = []
for i in range(l):
    time, direction = sys.stdin.readline().split()
    time = int(time)
    time_table.append((time, direction))

head_x = head_y = tail_x = tail_y = result = 0
direction = [0, 1]
direction_dictionary = {(0, 0): [0, 1]}
result = 0
for sec in range(1, 10001):
    result += 1
    direction_dictionary[(head_x, head_y)] = [direction[0], direction[1]]
    head_x += direction[0]
    head_y += direction[1]
    if head_x < 0 or head_y < 0 or head_x > n-1 or head_y > n-1:
        break
    if game_table[head_x][head_y] == 2:
        break
    elif game_table[head_x][head_y] == 1:
        game_table[head_x][head_y] = 2
    else:
        game_table[head_x][head_y] = 2
        game_table[tail_x][tail_y] = 0
        tail_direction = direction_dictionary[(tail_x, tail_y)]
        tail_x += tail_direction[0]
        tail_y += tail_direction[1]
    if len(time_table) > 0 and time_table[0][0] == sec:
        if direction[0] == 0 and time_table[0][1] == 'L':
            direction[1] *= -1
        elif direction[1] == 0 and time_table[0][1] == 'D':
            direction[0] *= -1
        direction[0], direction[1] = direction[1], direction[0]
        del time_table[0]
print(result)
