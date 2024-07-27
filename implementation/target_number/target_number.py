import sys
sys.setrecursionlimit(int(1e8))


def solution(numbers, target):
    answer = get_target(numbers, target)
    return answer


def get_target(numbers, target):
    if len(numbers) == 1:
        if numbers[0] == target or numbers[0] == -target:
            return 1
        else:
            return 0
    return get_target(numbers[1:], target-numbers[0]) + get_target(numbers[1:], target+numbers[0])


print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))
