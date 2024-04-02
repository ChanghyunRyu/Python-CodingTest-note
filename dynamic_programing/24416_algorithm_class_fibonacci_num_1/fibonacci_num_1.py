n = int(input())

arr = [1]*40
for i in range(2, n):
    arr[i] = arr[i-1] + arr[i-2]

print('{} {}'.format(arr[n-1], n-2))
