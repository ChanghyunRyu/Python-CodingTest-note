# 괄호를 적절히 쳐서 가장 적은 숫자를 만들어야 한다.
# 간단한 생각 = +를 해주는 수는 가장 작아야한다 => + 는 그대로 더한다.
# 간단한 생각2 = -를 해주는 수는 커야 한다. => - 뒤의 숫자는 -가 나올때까지 계속 더한다.
# 간단한 생각 결론: - 한 번 이상 나온다면 이후 숫자는 모두 빼기를 해줘도 된다.
# - 이후 + = ()를 통해 빼는 숫자를 크게
# - 이후 - = ()를 해주지 않아도 빼기가 된다.
equation = input()
result = start = 0
minus = False
for i in range(len(equation)):
    if equation[i] == '+' or equation[i] == '-':
        num = int(equation[start:i])
        if minus:
            result -= num
        else:
            result += num
        if equation[i] == '-':
            minus = True
        start = i+1
        continue
    if i == len(equation)-1:
        num = int(equation[start:i+1])
        if minus:
            result -= num
        else:
            result += num
print(result)
