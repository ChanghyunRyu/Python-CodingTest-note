import itertools


def solution(numbers):
    answer = set()
    for combination in itertools.combinations(numbers, 2):
        answer.add(combination[0]+combination[1])
    return sorted(list(answer))


print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
