import sys
n = int(input())
paper = []
for i in range(n):
    paper.append(list(map(int, sys.stdin.readline().split())))
minus = zero = plus = 0


def counting(x, y, length):
    global minus, zero, plus, paper
    num = paper[x][y]
    flag = False
    for i in range(length):
        for j in range(length):
            if paper[x+i][y+j] != num:
                flag = True
                break
        if flag:
            break
    if flag:
        cut = length//3
        counting(x, y, cut)
        counting(x + cut, y, cut)
        counting(x + (cut * 2), y, cut)
        counting(x, y + cut, cut)
        counting(x + cut, y + cut, cut)
        counting(x+(cut * 2), y + cut, cut)
        counting(x, y + (cut * 2), cut)
        counting(x + cut, y + (cut * 2), cut)
        counting(x + (cut * 2), y + (cut * 2), cut)
    else:
        if num == 1:
            plus += 1
        elif num == 0:
            zero += 1
        else:
            minus += 1


counting(0, 0, n)
print(minus)
print(zero)
print(plus)
