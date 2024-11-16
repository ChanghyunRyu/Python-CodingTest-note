def solution(string):
    stack = []
    for s in string:
        if s == '(':
            stack.append(s)
        elif s == ')':
            if not stack:
                return False
            if stack[-1] == '(':
                stack.pop()
            else:
                return False
    if stack:
        return False
    return True