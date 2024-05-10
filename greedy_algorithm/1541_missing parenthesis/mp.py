line = input()
result = 0
start = 0
minus = 1

for i in range(len(line)):
    if line[i] == '+' or line[i] == '-':
        number = int(line[start:i])
        result += minus*number
        start = i+1
    elif i == len(line)-1:
        number = int(line[start:i+1])
        result += minus * number
        start = i + 1
    if line[i] == '-':
        minus = -1
print(result)
