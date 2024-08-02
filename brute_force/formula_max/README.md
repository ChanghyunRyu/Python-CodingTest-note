## 수식 최대화

---

[출처] https://school.programmers.co.kr/learn/courses/30/lessons/67257

IT 벤처 회사를 운영하고 있는 라이언은 매년 사내 해커톤 대회를 개최하여 우승자에게 상금을 지급하고 있습니다.
이번 대회에서는 우승자에게 지급되는 상금을 이전 대회와는 다르게 다음과 같은 방식으로 결정하려고 합니다.

해커톤 대회에 참가하는 모든 참가자들에게는 숫자들과 3가지의 연산문자(+, -, *) 만으로 
이루어진 연산 수식이 전달되며, 참가자의 미션은 전달받은 수식에 포함된 연산자의 우
선순위를 자유롭게 재정의하여 만들 수 있는 가장 큰 숫자를 제출하는 것입니다.

단, 연산자의 우선순위를 새로 정의할 때, 같은 순위의 연산자는 없어야 합니다. 
즉, + > - > * 또는 - > * > + 등과 같이 연산자 우선순위를 정의할 수 있으나 
+,* > - 또는 * > +,-처럼 2개 이상의 연산자가 동일한 순위를 가지도록 연산자 우선순위를 정의할 수는 없습니다. 

수식에 포함된 연산자가 2개라면 정의할 수 있는 연산자 우선순위 조합은 2! = 2가지이며, 연
산자가 3개라면 3! = 6가지 조합이 가능합니다.
만약 계산된 결과가 음수라면 해당 숫자의 절댓값으로 변환하여 제출하며 
제출한 숫자가 가장 큰 참가자를 우승자로 선정하며, 우승자가 제출한 숫자를 우승상금으로 지급하게 됩니다.

참가자에게 주어진 연산 수식이 담긴 문자열 expression이 매개변수로 주어질 때, 
우승 시 받을 수 있는 가장 큰 상금 금액을 return 하도록 solution 함수를 완성해주세요.

---
### Problem Solved Check
- [X] 1회 24/06/16
- [X] 2회 24/08/02
- [ ] 3회

혼자서 풀지 못 했고, 책을 보고 후위 계산법이라는 형태로 푸는 방법을 학습했다.  
다음 학습 시에 해당 부분들을 해결해봐야 할 것으로 보인다.

1. 정규식을 이용하여 숫자와 연산자를 분리하는 방법
2. 우선 순위를 지정하여 중위 계산법을 후위 계산법으로 치환하는 방법
3. 치환한 후위 계산법을 통해 결과를 계산하는 방법

~~~
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
    
~~~
~~~
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
    
~~~
