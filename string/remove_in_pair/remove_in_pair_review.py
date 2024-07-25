def solution(s):
    stack = []
    for character in s:
        if stack and stack[-1] == character:
            stack.pop()
        else:
            stack.append(character)
    if stack:
        return 0
    return 1


print(solution('baabaa'))
