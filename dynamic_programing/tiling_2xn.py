n = int(input())
arr = [0 for i in range(n+1)]
for num in range(n+1):
    if num == 0:
        continue
    elif num == 1:
        arr[num] = 1
    elif num == 2:
        arr[num] = 2
    else:
        arr[num] = arr[num-1] + arr[num-2]

print(arr[n] % 10007)
