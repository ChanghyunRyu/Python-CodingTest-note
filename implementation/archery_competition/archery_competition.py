def solution(n, info):
    answer = [-1, [-1]]
    dfs(info, 0, [0]*11, n, answer)
    return answer[1]


def dfs(info, index, lion_arrow, remain, result):
    if index == 11 or remain < 0:
        return

    if index == 10 and remain >= 0:
        if remain > 0:
            lion_arrow[10] += remain
        score = calc_result(info, lion_arrow)
        if score <= 0:
            return
        if result[0] < score:
            result[0] = score
            result[1] = lion_arrow
        elif result[0] == score:
            result[1] = compare_result(result[1], lion_arrow)

    new_lion_arrow = list(lion_arrow)
    new_lion_arrow[index] = info[index]+1
    dfs(info, index + 1, new_lion_arrow, remain-(info[index]+1), result)
    dfs(info, index + 1, list(lion_arrow), remain, result)


def calc_result(info, result):
    apeach = 0
    lion = 0
    for i in range(len(info)):
        if info[i] == result[i] == 0:
            continue
        if info[i] < result[i]:
            lion += 10-i
        else:
            apeach += 10-i
    return lion-apeach


def compare_result(before, after):
    for i in range(10, 0, -1):
        if before[i] > after[i]:
            return before
        elif after[i] > before[i]:
            return after


print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))
print(solution(1, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
print(solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]))
print(solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]))
print(solution(3, [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0]))
