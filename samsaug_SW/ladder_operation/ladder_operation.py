import sys


n, m, h = map(int, sys.stdin.readline().split())
ladders = [[0]*n for _ in range(h)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    ladders[a-1][b-1] = 1


def check_problem(number, ladder):
    for idx in range(number):
        start = idx
        for height in range(len(ladder)):
            if ladder[height][start] == 1:
                start += 1
            elif start > 0 and ladder[height][start-1] == 1:
                start -= 1
        if start != idx:
            return False
    return True


def dfs(count, x, ladder):
    global answer
    if answer <= count:
        return
    if check_problem(len(ladder[0]), ladder):
        answer = min(answer, count)
        return
    if count >= 3:
        return
    for i in range(x, len(ladder)):
        for j in range(0, len(ladder[0])-1):
            check_left = j == 0 or ladder[i][j-1] == 0
            check_right = ladder[i][j+1] == 0
            if ladder[i][j] == 0 and check_left and check_right:
                ladder[i][j] = 1
                dfs(count+1, i, ladder)
                ladder[i][j] = 0


answer = 4
dfs(0, 0, ladders)
if answer > 3:
    answer = -1
print(answer)
