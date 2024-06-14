def solution(user_id, banned_id):
    stack = [([], 0, user_id)]
    result = []
    while stack:
        result_list, index, user_list = stack.pop()
        if index == len(banned_id):
            result_list.sort()
            if result_list not in result:
                result.append(result_list)
            continue
        for user in user_list:
            if check_id(banned_id[index], user):
                next_result_list = list(result_list)
                next_result_list.append(user)
                next_user_list = list(user_list)
                next_user_list.remove(user)
                stack.append((next_result_list, index+1, next_user_list))
    return len(result)


def check_id(ban_id, chk_id):
    if len(ban_id) != len(chk_id):
        return False
    for i in range(len(ban_id)):
        if ban_id[i] == '*':
            continue
        if ban_id[i] != chk_id[i]:
            return False
    return True


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
