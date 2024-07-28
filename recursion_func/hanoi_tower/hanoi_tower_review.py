def solution(n):
    answer = []
    hanoi(1, 2, 3, n, answer)
    return answer


def hanoi(start, mid, end, num, result):
    if num == 1:
        result.append([start, end])
    else:
        hanoi(start, end, mid, num-1, result)
        result.append([start, end])
        hanoi(mid, start, end, num-1, result)


print(solution(2))
