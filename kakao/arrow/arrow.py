import sys
sys.setrecursionlimit(10000)


def solution(n, info):
    answer = [-1]
    dfs(answer, [], 0, info, n, True)
    dfs(answer, [], 0, info, n, False)
    if answer[0] == -1:
        return answer
    else:
        return answer[0]


def dfs(answer, result, idx, info, arrows, win_lose):
    if idx == len(info) - 1:
        result.append(arrows)
        score = calc_score(info, result)
        if score > 0:
            if answer[0] == -1:
                answer[0] = result
            else:
                score2 = calc_score(info, answer[0])
                if score > score2:
                    answer[0] = result
                elif score == score2:
                    # 기존: answer[0], 비교: result
                    for i in range(len(result)):
                        if answer[0][10 - i] < result[10 - i]:
                            answer[0] = result
                            break
                        elif answer[0][10 - i] == result[10 - i]:
                            continue
                        else:
                            break
        return
    if win_lose:
        if info[idx] < arrows:
            arrows -= info[idx] + 1
            result.append(info[idx] + 1)
        else:
            result.append(0)
        if arrows > 0:
            dfs(answer, list(result), idx + 1, info, arrows, True)
        dfs(answer, list(result), idx + 1, info, arrows, False)
    else:
        result.append(0)
        if arrows > 0:
            dfs(answer, list(result), idx + 1, info, arrows, True)
        dfs(answer, list(result), idx + 1, info, arrows, False)


def calc_score(a, r):
    apeach = 0
    rion = 0
    for i in range(len(a)):
        if a[i] == 0 and r[i] == 0:
            continue
        if a[i] < r[i]:
            rion += 10 - i
        else:
            apeach += 10 - i
    return rion - apeach