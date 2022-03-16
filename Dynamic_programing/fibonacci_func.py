import sys

t = int(input())
arr = []
for i in range(t):
    arr.append(int(sys.stdin.readline()))

col_arr = []
for j in range(41):
    temp = [-1, -1]
    col_arr.append(temp)

for num in range(41):
    if num == 0:
        col_arr[num] = [1, 0]
    elif num == 1:
        col_arr[num] = [0, 1]
    else:
        col_arr[num][0] = col_arr[num-1][0] + col_arr[num-2][0]
        col_arr[num][1] = col_arr[num - 1][1] + col_arr[num - 2][1]

for n in arr:
    print('{} {}'.format(col_arr[n][0], col_arr[n][1]))
