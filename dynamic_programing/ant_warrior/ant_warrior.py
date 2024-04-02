n = int(input())

arr = list(map(int, input().split()))
result = [0]*(n+1)
result[1] = arr[0]

for i in range(2, len(arr)+1):
    result[i] = max((result[i-2]+arr[i-1]), result[i-1])

print(result[n])
