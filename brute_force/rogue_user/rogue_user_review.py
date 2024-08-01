import itertools


def solution(user_id, banned_id):
    answer = set()
    for permutation in itertools.permutations(user_id, len(banned_id)):
        permutation = list(permutation)
        flag = True
        for i in range(len(permutation)):
            if not match_user_id(permutation[i], banned_id[i]):
                flag = False
                break
        if flag:
            answer.add(''.join(sorted(permutation)))
    return len(answer)


def match_user_id(user_id, banned_id):
    if len(user_id) != len(banned_id):
        return False
    for i in range(len(user_id)):
        if banned_id[i] == '*':
            continue
        if user_id[i] != banned_id[i]:
            return False
    return True


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))
