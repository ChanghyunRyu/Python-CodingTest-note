import itertools


def solution(user_id, banned_id):
    answer = set()
    for per in itertools.permutations(user_id, len(banned_id)):
        is_collect = True
        for i in range(len(banned_id)):
            if not check_id(per[i], banned_id[i]):
                is_collect = False
                break
        per = sorted(per)
        if is_collect:
            answer.add(''.join(per))
    return len(answer)


def check_id(user_id, banned_id):
    if len(user_id) != len(banned_id):
        return False
    for i in range(len(user_id)):
        if banned_id[i] != '*' and user_id[i] != banned_id[i]:
            return False
    return True


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],  ["fr*d*", "*rodo", "******", "******"]))
