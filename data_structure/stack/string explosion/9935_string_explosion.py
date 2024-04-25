arr = input()
ex = input()

temp = []
ex_len = len(ex)

for i in range(len(arr)):
    temp.append(arr[i])
    if ''.join(temp[-ex_len:]) == ex:
        for _ in range(ex_len):
            temp.pop()

if temp:
    print(''.join(temp))
else:
    print('FRULA')
