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
