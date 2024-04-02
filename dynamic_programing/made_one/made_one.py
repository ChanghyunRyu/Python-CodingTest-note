x = int(input())

arr = [0]*30001
arr[1], arr[2] = 1, 1

for i in range(3, x):
    result = arr[i-1]
    if i % 5 == 0:
        result = min(result, arr[i//5])
    elif i % 3 == 0:
        result = min(result, arr[i//3])
    elif i % 2 == 0:
        result = min(result, arr[i//2])
    arr[i] = result + 1

print(arr[x-1])
