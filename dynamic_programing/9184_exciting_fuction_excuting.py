import sys

# 0 = -50, 50 = 0, 100 = 50
w = [[[0]*21 for i in range(101)] for j in range(101)]


def solution_func(a, b, c):
    global w
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        w[20][20][20] = solution_func(20, 20, 20)
        return w[20][20][20]
    if w[a][b][c] != 0:
        return w[a][b][c]
    else:
        if a < b < c:
            w[a][b][c] = solution_func(a, b, c-1) + solution_func(a, b-1, c-1) - solution_func(a, b-1, c)
        else:
            w[a][b][c] = solution_func(a-1, b, c) + solution_func(a-1, b-1, c) + solution_func(a-1, b, c-1) \
                         - solution_func(a-1, b-1, c-1)
        return w[a][b][c]


test_list = []
while True:
    num1, num2, num3 = map(int, sys.stdin.readline().split())
    if num1 == num2 == num3 == -1:
        break
    test_list.append((num1, num2, num3))
for test in test_list:
    num1, num2, num3 = test[0], test[1], test[2]
    print('w({}, {}, {}) = {}'.format(num1, num2, num3, solution_func(num1, num2, num3)))
