import heapq


def solution(name):
    change_character = 0
    targets = set()
    for i in range(len(name)):
        step_forward = ord(name[i])-ord('A')
        step_backward = abs(26-step_forward)
        change_character += min(step_forward, step_backward)
        if step_forward != 0:
            targets.add(i)

    queue = [(0, 0, targets)]
    while queue:
        result, now, targets = heapq.heappop(queue)
        if not targets:
            break
        for target in targets:
            new_targets = set(targets)
            new_targets.remove(target)
            forward = abs(target-now)
            backward = abs(len(name)-forward)
            heapq.heappush(queue, (result+min(forward, backward), target, new_targets))
    return change_character+result


print(solution("JEROEN"))
print(solution("JAN"))
print(solution("BAAAAABAA"))
print(solution("BBBABAABABABB"))
print(solution("BBABAAAAAAB"))
print(solution("BABBAABB"))
print(solution("BBAAAAAAABAB"))
print(solution("BAABBAAA"))
