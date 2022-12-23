# 어째서 스택을 사용하는 문제인지 고민을 조금 했던 문제입니다.
# 언제나 괄호 문자열은 한 쌍을 이룬다는 점, ')' 문자가 나왔다면 그 짝은 가장 최근에 사용된 '(' 라는 점
# 두 가지를 통해 스택 구조를 사용하여 문제를 풀었습니다.

import sys
start_bracket = []
results = []

t = int(input())
for i in range(t):
    start_bracket.clear()
    flag = True
    input_string = sys.stdin.readline()
    for char in input_string:
        if char == '(':
            start_bracket.append(char)
        elif char == ')':
            if len(start_bracket) != 0:
                start_bracket.pop()
            else:
                flag = False
                break
    if len(start_bracket) != 0:
        flag = False
    if flag:
        print("YES")
    else:
        print("NO")
