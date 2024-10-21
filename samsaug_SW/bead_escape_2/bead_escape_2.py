def dfs(command, red, blue, hole, board, count, before_points, answer):
    if count > 10:
        return
    dx, dy = set_dxy(command)
    r_x, r_y = red
    b_x, b_y = blue
    flag = True
    b_in_hole = False
    r_in_hole = False
    while flag:
        flag = False
        b_nx = b_x + dx
        b_ny = b_y + dy
        if (b_nx, b_ny) == hole:
            b_in_hole = True
        if board[b_nx][b_ny] == 0 and (b_nx, b_ny) != (r_x, r_y):
            flag = True
            b_x = b_nx
            b_y = b_ny

        r_nx = r_x + dx
        r_ny = r_y + dy
        if (r_nx, r_ny) == hole:
            r_in_hole = True
        if board[r_nx][r_ny] == 0 and (r_nx, r_ny) != (b_x, b_y):
            flag = True
            r_x = r_nx
            r_y = r_ny
    if b_in_hole:
        return
    if r_in_hole:
        answer.append(count)
        return
    rb_point = ((r_x, r_y), (b_x, b_y))
    if rb_point in before_points:
        if before_points[rb_point] <= count:
            return
        else:
            before_points[rb_point] = count
    else:
        before_points[rb_point] = count

    dfs('UP', (r_x, r_y), (b_x, b_y), hole, board, count + 1, before_points, answer)
    dfs('DOWN', (r_x, r_y), (b_x, b_y), hole, board, count + 1, before_points, answer)
    dfs('LEFT', (r_x, r_y), (b_x, b_y), hole, board, count + 1, before_points, answer)
    dfs('RIGHT', (r_x, r_y), (b_x, b_y), hole, board, count + 1, before_points, answer)


def set_dxy(command):
    if command == 'UP':
        return -1, 0
    elif command == 'DOWN':
        return 1, 0
    elif command == 'LEFT':
        return 0, -1
    elif command == 'RIGHT':
        return 0, 1


n, m = map(int, input().split())
bead_map = [[1]*m for _ in range(n)]

R_point = (0, 0)
B_point = (0, 0)
hole = (0, 0)
for i in range(n):
    line = input()
    for j in range(len(line)):
        if line[j] == '.':
            bead_map[i][j] = 0
        elif line[j] == 'R':
            bead_map[i][j] = 0
            R_point = (i, j)
        elif line[j] == 'B':
            bead_map[i][j] = 0
            B_point = (i, j)
        elif line[j] == 'O':
            bead_map[i][j] = 0
            hole = (i, j)

record = {(R_point, B_point): 0}
answer = [11]
dfs('UP', R_point, B_point, hole, bead_map, 1, record, answer)
dfs('DOWN', R_point, B_point, hole, bead_map, 1, record, answer)
dfs('LEFT', R_point, B_point, hole, bead_map, 1, record, answer)
dfs('RIGHT', R_point, B_point, hole, bead_map, 1, record, answer)
result = min(answer)
if result > 10:
    print(-1)
else:
    print(result)
