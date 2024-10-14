import math


def solution(n, k):
    answer = []
    k -= 1
    numbers = list(range(1, n+1))
    for i in range(n, 0, -1):
        idx, k = return_number(i, k)
        answer.append(numbers[idx])
        del numbers[idx]
    return answer


def return_number(n, k):
    f = math.factorial(n-1)
    index, remain = divmod(k, f)
    return index, remain


print(solution(3, 5))
