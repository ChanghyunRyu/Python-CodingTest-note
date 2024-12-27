def solution(n, m, x, y, r, c, k):
    answer = []
    now_x = x
    now_y = y
    for i in range(k, 0, -1):
        distance = abs(now_x-r) + abs(now_y-c)
        if distance == i:
            answer += get_shortest_path(now_x, now_y, r, c)
            return ''.join(answer)
        elif distance > i:
            answer = 'impossible'
            return answer
        if now_x < n:
            now_x += 1
            answer.append('d')
            continue
        elif now_y > 1:
            now_y -= 1
            answer.append('l')
            continue
        if now_x == n and now_y == 1:
            short_path = get_shortest_path(n, 1, r, c)
            remain = i - len(short_path)
            if remain % 2 == 1:
                answer = 'impossible'
                return answer
            else:
                answer += ['r', 'l']*(remain//2)
                answer += short_path
                return ''.join(answer)


def get_shortest_path(x, y, r, c):
    result = []
    up_down = x-r
    left_right = y-c
    if left_right > 0:
        result += ['l']*left_right
    else:
        result += ['r']*abs(left_right)
    if up_down > 0:
        result += ['u']*up_down
    else:
        result += ['d']*abs(up_down)
    result.sort()
    return result


print(solution(3, 4, 2, 3, 3, 1, 5))
print(solution(3, 3, 1, 2, 3, 3, 4))
