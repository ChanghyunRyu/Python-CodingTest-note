n = int(input())


def create_star(num, is_blank):
    if is_blank:
        return [[0]*num for _ in range(num)]
    if num == 3:
        return [[1, 1, 1],
                [1, 0, 1],
                [1, 1, 1]]
    temp = [[0]*num for _ in range(num)]
    for i in range(3):
        for j in range(3):
            start_x = i*(num//3)
            start_y = j*(num//3)
            if i == 1 and j == 1:
                star_arr = create_star(num//3, True)
            else:
                star_arr = create_star(num//3, False)
            for x in range(len(star_arr)):
                for y in range(len(star_arr)):
                    nx = start_x+x
                    ny = start_y+y
                    temp[nx][ny] = star_arr[x][y]
    return temp


arr = create_star(n, False)
for line in arr:
    for num in line:
        if num == 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()
