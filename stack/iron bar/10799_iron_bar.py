bar = input()
tmp = [bar[0]]
result = 0
for i in range(1, len(bar)):
    if bar[i] == '(':
        tmp.append(bar[i])
    else:
        if bar[i-1] == '(':
            tmp.pop()
            result += len(tmp)
        else:
            tmp.pop()
            result += 1
print(result)
