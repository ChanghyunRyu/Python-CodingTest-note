arr = input()
ex = input()

temp = []
arr_len = len(arr)

for i in range(len(arr)):
    temp.append(arr[i])
    if ''.join(temp[-arr_len:]) == ex:
        for _ in range(arr_len):
            temp.pop()

if temp:
    print(''.join(temp))
else:
    print('FRULA')
