def solution(answers):
    m1 = [1, 2, 3, 4, 5]
    m2 = [2, 1, 2, 3, 2, 4, 2, 5]
    m3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    answer = []
    r1 = scoring(answers, m1)
    r2 = scoring(answers, m2)
    r3 = scoring(answers, m3)

    result = max(r1, r2, r3)
    if r1 == result:
        answer.append(1)
    if r2 == result:
        answer.append(2)
    if r3 == result:
        answer.append(3)
    return answer


def scoring(answers, method):
    result = 0
    for i in range(len(answers)):
        index = i % len(method)
        if answers[i] == method[index]:
            result += 1
    return result


print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))
