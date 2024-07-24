from math import factorial


def solution(n, k):
    answer = []
    numbers = list(range(1, n+1))
    k -= 1
    while numbers:
        idx, k = divmod(k, factorial(len(numbers)-1))
        answer.append(numbers.pop(idx))
    return answer


print(solution(3, 5))
