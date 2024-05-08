import sys
from bisect import bisect_left

n = int(input())
cords = []
for _ in range(n):
    cords.append(list(map(int, sys.stdin.readline().split())))
cords.sort()

dp = [0]*n
dp[0] = 1
A = [cords[0][1]]
for i in range(1, n):
    _, num = cords[i]
    if num > A[len(A)-1]:
        A.append(num)
        dp[i] = len(A)
    else:
        pos = bisect_left(A, num)
        dp[i] = pos
        if A[pos] > num:
            A[pos] = num
print(n-len(A))
