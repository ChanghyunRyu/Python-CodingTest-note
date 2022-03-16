import sys

t = int(input())
n_arr = []
for i in range(t):
    n_arr.append(int(sys.stdin.readline()))
col_arr = [0 for i in range(11)]
for num in range(len(col_arr)):
    if num == 0:
        continue
    elif num == 1:
        col_arr[num] = 1
    elif num == 2:
        col_arr[num] = 2
    elif num == 3:
        col_arr[num] = 4
    else:
        col_arr[num] = col_arr[num-1] + col_arr[num-2] + col_arr[num-3]

for n in n_arr:
    print(col_arr[n])
