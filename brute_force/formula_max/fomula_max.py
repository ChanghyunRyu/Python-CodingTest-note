from itertools import permutations
import re


def solution(expression):
    answer = 0
    tokens = re.split('([-+*])', expression)
    operator = ['*', '-', '+']
    for i in map(list, permutations(operator, 3)):
        priority = {o: p for p, o in enumerate(list(i))}
        postfix = to_post_fix(tokens, priority)
        answer = max(answer, abs(calc(postfix)))
    return answer


def to_post_fix(tokens, priority):
    stack = []
    postfix = []
    for token in tokens:
        if token.isdigit():
            postfix.append(token)
        else:
            if not stack:
                stack.append(token)
            else:
                while stack:
                    if priority[token] <= priority[stack[-1]]:
                        postfix.append(stack.pop())
                    else:
                        break
                stack.append(token)
    while stack:
        postfix.append(stack.pop())
    return postfix


def calc(tokens):
    stack = []
    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
            continue
        num1 = stack.pop()
        num2 = stack.pop()
        if token == '*':
            stack.append(num2*num1)
        if token == '+':
            stack.append(num2+num1)
        if token == '-':
            stack.append(num2-num1)
    return stack.pop()


print(solution("100-200*300-500+20"))
