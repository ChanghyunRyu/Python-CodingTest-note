n = int(input())
number_table = list(map(int, input().split()))

now_number = 1
stack = []
idx = 0

while idx < n or stack:
    if stack and stack[-1] == now_number:
        now_number += 1
        stack.pop()
        continue

    if idx >= n:
        break
    if number_table[idx] == now_number:
        now_number += 1
    else:
        stack.append(number_table[idx])
    idx += 1

if now_number == n+1:
    print('Nice')
else:
    print('Sad')
