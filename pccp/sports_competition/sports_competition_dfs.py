def dfs(ability, result, depth, visited, score):
    if depth == len(ability[0]):
        result.append(score)
        return
    for student in range(len(ability)):
        if visited[student]:
            continue
        visited[student] = True
        dfs(ability, result, depth+1, visited, score+ability[student][depth])
        visited[student] = False


def solution(ability):
    answer = []
    dfs(ability, answer, 0, [False]*(len(ability)), 0)
    return max(answer)


print(solution([[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]))
