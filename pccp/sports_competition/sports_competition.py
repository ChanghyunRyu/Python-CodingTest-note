import itertools


def solution(ability):
    answer = 0
    for c in itertools.combinations(ability, len(ability[0])):
        score = return_max_score(c)
        answer = max(score, answer)
    return answer


def return_max_score(students):
    num = len(students)
    result = 0
    for p in itertools.permutations(range(num), num):
        score = 0
        for i in range(len(p)):
            score += students[i][p[i]]
        result = max(result, score)
    return result


print(return_max_score([[40, 10, 10], [20, 5, 0], [30, 30, 30]]))
print(solution([[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]))
print(solution([[20, 30], [30, 20], [20, 30]]))
