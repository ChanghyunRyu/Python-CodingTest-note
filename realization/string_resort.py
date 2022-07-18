number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
s = list(input())
s.sort()
s_num = []
for c in s:
    if c in number:
        s_num.append(c)
    else:
        print(c, end='')
result = 0
for num in s_num:
    result += int(num)
print(result)
