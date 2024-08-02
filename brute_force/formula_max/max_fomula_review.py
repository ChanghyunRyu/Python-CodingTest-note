import re
import itertools


def get_postfix_expression(s, formula):
    tokens = re.split('([-+*])', s)
    postfix = []
    stack = []
    for token in tokens:
        if token.isdigit():
            postfix.append(token)
        else:
            if not stack or formula[token] > formula[stack[-1]]:
                stack.append(token)
                continue
            while stack and formula[stack[-1]] >= formula[token]:
                postfix.append(stack.pop())
            stack.append(token)
    while stack:
        postfix.append(stack.pop())
    return postfix


def calc_postfix_expression(expression):
    stack = []
    for token in expression:
        if token.isdigit():
            stack.append(token)
        else:
            num1 = int(stack.pop())
            num2 = int(stack.pop())
            result = 0
            if token == '*':
                result = num1 * num2
            elif token == '-':
                result = num2 - num1
            elif token == '+':
                result = num1 + num2
            stack.append(result)
    return stack[0]


def create_formula():
    operators = ['+', '-', '*']
    result = []
    for permutation in itertools.permutations(operators, 3):
        formula = {}
        for i, operator in enumerate(list(permutation)):
            formula[operator] = i
        result.append(formula)
    return result


def solution(expression):
    formulas = create_formula()
    answer = 0
    for formula in formulas:
        postfix_expression = get_postfix_expression(expression, formula)
        answer = max(answer, abs(calc_postfix_expression(postfix_expression)))
    return answer


print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))
