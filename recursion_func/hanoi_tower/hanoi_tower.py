def solution(n):
    answer = []
    hanoi(answer, n, 1, 2, 3)
    return answer


def hanoi(result, num, start, mid, end):
    if num == 1:
        result.append([start, end])
    else:
        hanoi(result, num-1, start, end, mid)
        result.append([start, end])
        hanoi(result, num-1, mid, start, end)


print(solution(2))
print(solution(3))
