import sys

n = int(input())
blue = 0
white = 0
paper = []
for i in range(n):
    paper.append(list(map(int, sys.stdin.readline().split())))


def cutting(x, y, length):
    global blue, white, paper
    color = paper[x][y]
    flag = False
    for i in range(length):
        for j in range(length):
            if paper[x+i][y+j] != color:
                flag = True
                break
        if flag:
            break
    if flag:
        cut = length//2
        cutting(x, y, cut)
        cutting(x+cut, y, cut)
        cutting(x, y+cut, cut)
        cutting(x+cut, y+cut, cut)
    else:
        if color == 0:
            white += 1
        else:
            blue += 1


cutting(0, 0, n)
print(white)
print(blue)
