def solution(s):
    answer = 0
    stack = []
    for case in s:
        if stack and stack[-1] == case:
            stack.pop()
        else:
            stack.append(case)
    if not stack:
        answer = 1
    return answer


print(solution('baabaa'))
print(solution('cdcd'))
print(solution('aa'))
