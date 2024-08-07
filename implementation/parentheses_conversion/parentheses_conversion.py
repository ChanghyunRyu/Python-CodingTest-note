import sys
sys.setrecursionlimit(10**6)


def solution(p):
    answer = conversion_parentheses(p)
    return answer


def conversion_parentheses(w):
    if w == '':
        return w
    open_p = close_p = 0
    idx = 0
    for i in range(len(w)):
        if w[i] == '(':
            open_p += 1
        elif w[i] == ')':
            close_p += 1
        if open_p == close_p:
            idx = i
            break
    u, v = w[:idx+1], w[idx+1:]
    if not check_correct_parentheses(u):
        temp = ['(', conversion_parentheses(v), ')']
        u = u[1:len(u)-1]
        new_u = []
        for i in range(len(u)):
            if u[i] == '(':
                new_u.append(')')
            else:
                new_u.append('(')
        new_u = ''.join(new_u)
        temp.append(new_u)
        return ''.join(temp)
    return ''.join([u, conversion_parentheses(v)])


def check_correct_parentheses(p):
    stack = []
    for i in range(len(p)):
        if p[i] == '(':
            stack.append(p[i])
        else:
            if stack:
                stack.pop()
            else:
                return False
    if stack:
        return False
    return True


print(solution("(()())()"))
print(solution(')('))
print(solution("()))((()"))
