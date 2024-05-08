import sys


def binary_search(target, arr):
    start, end = 0, len(arr)-1
    while start < end:
        mid = (start+end)//2
        if target > arr[mid]:
            start = mid+1
        else:
            end = mid
    return end


n = int(input())
cords = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    cords.append((a, b))
cords.sort()

dp = [0]*n
dp[0] = 1
A = [cords[0][1]]
for i in range(1, len(cords)):
    _, num = cords[i]
    if num > A[len(A)-1]:
        A.append(num)
        dp[i] = len(A)
    else:
        pos = binary_search(num, A)
        dp[i] = dp[pos]
        if A[pos] > num:
            A[pos] = num
print(n-len(A))
