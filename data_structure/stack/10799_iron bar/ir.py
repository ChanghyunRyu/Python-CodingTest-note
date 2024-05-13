line = input()
result = 0
count = 0
for i in range(len(line)):
    if line[i] == '(':
        count += 1
    elif line[i] == ')':
        if line[i-1] == '(':
            count -= 1
            result += count
        else:
            result += 1
            count -= 1
print(result)
