from collections import defaultdict


n, m = map(int, input().split())
arr =[]
for _ in range(n):
    arr.append(input())


def get_right(x, y, count):
    if arr[x][y] == '#':
        count += 1
    y += 1
    if 0 <= y < m:
        return get_right(x, y, count)
    else:
        return count


def get_down(x, y, count):
    if arr[x][y] == '#':
        count += 1
    x += 1
    if 0 <= x < n:
        return get_down(x, y, count)
    else:
        return count


answer = 'RIGHT'
flag = False
for i in range(n):
    for j in range(m):
        if arr[i][j] == '#':
            top = get_right(i, j, 0)
            left = get_down(i, j, 0)
            if top > left:
                answer = 'LEFT'
            elif left > top:
                answer = 'UP'
            else:
                right = get_down(i, j+top-1, 0)
                bottom = get_right(i+left-1, j, 0)
                if right > bottom:
                    answer = 'DOWN'
            flag = True
            break
    if flag:
        break
print(answer)
