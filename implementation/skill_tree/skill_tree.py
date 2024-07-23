def solution(skill, skill_trees):
    answer = 0
    dictionary = skill_to_num(skill)
    for skilltree in skill_trees:
        if check_skilltree(dictionary, skilltree):
            answer += 1
    return answer


def check_skilltree(dictionary, skill_tree):
    now_step = 0
    for skill in skill_tree:
        if skill in dictionary:
            if dictionary[skill] == now_step:
                now_step += 1
            else:
                return False
    return True


def skill_to_num(skill):
    result = {}
    for i in range(len(skill)):
        result[skill[i]] = i
    return result


print(solution('CBD', ["BACDE", "CBADF", "AECB", "BDA"]))
