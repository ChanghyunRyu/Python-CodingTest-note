def solution(line):
    answer = []
    point = []
    x_min = y_min = int(1e15)
    x_max= y_max = -int(1e15)
    for i in range(len(line)-1):
        for j in range(i+1, len(line)):
            a, b, e = line[i]
            c, d, f = line[j]
            if a*d != b*c:
                # 교점 x, y 좌표 구하기
                x = float((b*f-e*d)/(a*d-b*c))
                y = float((e*c-a*f)/(a*d-b*c))
                if x.is_integer() and y.is_integer():
                    x = int(x)
                    y = int(y)
                    point.append([x, y])
                    if x_min > x:
                        x_min = x
                    if y_min > y:
                        y_min = y
                    if x_max < x:
                        x_max = x
                    if y_max < y:
                        y_max = y
    tmp = [['.']*(x_max-x_min+1) for _ in range(y_max-y_min+1)]
    for pos_x, pos_y in point:
        nx = pos_x - x_min
        ny = pos_y - y_min
        tmp[ny][nx] = '*'
    for t in tmp:
        answer.append(''.join(t))
    return answer[::-1]


temp = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]
print(solution(temp))
