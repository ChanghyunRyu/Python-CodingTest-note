equation = input()

result = 0
start = 0
minus = False
for i in range(len(equation)):
    if equation[i] == '-' or equation[i] == '+':
        number = int(equation[start:i])
        start = i+1
        if minus:
            result = result - number
        else:
            result = result + number
        if equation[i] == '-':
            minus = True
        continue
    if i == len(equation) - 1:
        number = int(equation[start:i+1])
        if minus:
            result = result - number
        else:
            result = result + number
        if equation[i] == '-':
            minus = True
print(result)
