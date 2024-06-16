from itertools import permutations
import re


def solution(expression):
    answer = 0
    # 토큰 분할
    tokens = exp_to_token(expression)
    # 순열을 이용한 우선 순위들 생성
    priorities = create_formula_priority()
    for priority in priorities:
        # 우선 순위에 맞게 후위 계산식 생성
        postfix_tokens = mid_to_postfix(tokens, priority)
        # 후위 계산식 통해 계산
        result = calc_postfix(postfix_tokens)
        answer = max(answer, abs(result))
    return answer


def exp_to_token(expression):
    tokens = re.split('([-+*])', expression)
    return tokens


def create_formula_priority():
    formulas = ['*', '+', '-']
    permutation = map(list, permutations(formulas, 3))
    priorities = []
    for p in permutation:
        priority = {formula: number for number, formula in enumerate(p)}
        priorities.append(priority)
    return priorities


def mid_to_postfix(tokens, priority):
    new_tokens = []
    formula_stack = []
    for token in tokens:
        if token.isdigit():
            new_tokens.append(token)
            continue

        if not formula_stack:
            formula_stack.append(token)
        else:
            while formula_stack:
                if priority[token] > priority[formula_stack[-1]]:
                    break
                else:
                    new_tokens.append(formula_stack.pop())
            formula_stack.append(token)
    while formula_stack:
        new_tokens.append(formula_stack.pop())
    return new_tokens


def calc_postfix(tokens):
    calc_stack = []
    for token in tokens:
        if token.isdigit():
            calc_stack.append(int(token))
            continue
        num1 = calc_stack.pop()
        num2 = calc_stack.pop()
        if token == '*':
            calc = num1*num2
        elif token == '+':
            calc = num1+num2
        elif token == '-':
            calc = num2-num1
        calc_stack.append(calc)
    return calc_stack.pop()


print(solution("100-200*300-500+20"))
