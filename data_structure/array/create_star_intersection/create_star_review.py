from itertools import combinations


def find_intersection(line1, line2):
    a, b, e = line1[0], line1[1], line1[2]
    c, d, f = line2[0], line2[1], line2[2]
    if a*d-b*c != 0:
        x = (b*f-e*d)/(a*d-b*c)
        y = (e*c-a*f)/(a*d-b*c)
    else:
        x = y = False
    return x, y


def solution(lines):
    intersections = []
    x_min = y_min = int(1e15)
    x_max = y_max = -int(1e15)
    for combination in combinations(lines, 2):
        i_x, i_y = find_intersection(combination[0], combination[1])
        if i_x is not False and i_x.is_integer() and i_y.is_integer():
            i_x, i_y = int(i_x), int(i_y)
            if i_x < x_min:
                x_min = i_x
            if i_x > x_max:
                x_max = i_x
            if i_y < y_min:
                y_min = i_y
            if i_y > y_max:
                y_max = i_y
            intersections.append((i_x, i_y))
    answer = [['.']*(x_max-x_min+1) for _ in range(y_max-y_min+1)]
    for x, y in intersections:
        d_x = x-x_min
        d_y = abs(y_min-y)
        answer[d_y][d_x] = '*'
    result = []
    for line in answer:
        result.append(''.join(line))
    return result[::-1]


print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))
print(solution([[1, -1, 0], [2, -1, 0]]))
