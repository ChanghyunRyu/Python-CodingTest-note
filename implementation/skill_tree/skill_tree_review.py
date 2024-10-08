def solution(skill, skill_trees):
    answer = 0
    route = {}
    for i in range(len(skill)):
        route[skill[i]] = i
    for skill_tree in skill_trees:
        if check_skilltree(skill_tree, route):
            answer += 1
    return answer


def check_skilltree(skill_tree, route):
    step = 0
    for s in skill_tree:
        if s not in route:
            continue
        if step != route[s]:
            return False
        step += 1
    return True


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
