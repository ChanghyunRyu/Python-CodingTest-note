def solution(n):
    answer = []
    move_hanoi(1, 2, 3, n, answer)
    return answer


def move_hanoi(start, middle, end, n, result):
    if n == 1:
        result.append([start, end])
    else:
        move_hanoi(start, end, middle, n - 1, result)
        result.append([start, end])
        move_hanoi(middle, start, end, n - 1, result)


print(solution(2))
print(solution(15))
