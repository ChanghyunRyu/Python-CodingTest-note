n = int(input())
video = []
for i in range(n):
    video.append(input())


def quadTree(x, y, length):
    global video
    data = video[x][y]
    flag = False
    for i in range(length):
        for j in range(length):
            if video[x+i][y+j] != data:
                flag = True
                break
        if flag:
            break
    if flag:
        cut = length//2
        string = '(' + quadTree(x, y, cut) + quadTree(x, y+cut, cut) + quadTree(x+cut, y, cut) + quadTree(x+cut, y+cut, cut) + ')'
        return string
    else:
        return str(data)


print(quadTree(0, 0, n))
