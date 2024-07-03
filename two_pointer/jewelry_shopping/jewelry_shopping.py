def solution(gems):
    answer = [0, len(gems) - 1]
    kind = len(set(gems))

    gems_dict = {gems[0]: 1}
    start = end = 0
    while end < len(gems):
        if len(gems_dict) < kind:
            end += 1
            if end >= len(gems):
                break
            if gems[end] not in gems_dict:
                gems_dict[gems[end]] = 1
            else:
                gems_dict[gems[end]] += 1
        else:
            if end-start < answer[1]-answer[0]:
                answer = [start, end]
            if gems_dict[gems[start]] == 1:
                del gems_dict[gems[start]]
            else:
                gems_dict[gems[start]] -= 1
            start += 1

    answer[0] += 1
    answer[1] += 1

    return answer


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
