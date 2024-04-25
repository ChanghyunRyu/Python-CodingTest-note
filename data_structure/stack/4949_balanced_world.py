import sys

while True:
    flag = True
    brackets =[]
    input_string = sys.stdin.readline()
    if input_string == '.\n':
        break
    for char in input_string:
        if char == '(' or char == '[':
            brackets.append(char)
        if char == ')':
            if len(brackets) != 0:
                if brackets.pop() != '(':
                    flag = False
                    break
            else:
                flag = False
                break
        if char == ']':
            if len(brackets) != 0:
                if brackets.pop() != '[':
                    flag = False
                    break
            else:
                flag = False
                break
    if len(brackets) != 0:
        flag = False
    if flag:
        print('yes')
    else:
        print('no')
