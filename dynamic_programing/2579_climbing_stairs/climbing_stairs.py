import sys

n = int(input())
stairs = []
for _ in range(n):
    stairs.append(int(sys.stdin.readline().rstrip()))

dp = [0]*(n+1)
dp[1] = stairs[0]
if n >= 2:
    dp[2] = stairs[0]+stairs[1]
    for i in range(3, n+1):
        dp[i] = max(dp[i-3]+stairs[i-2]+stairs[i-1], dp[i-2]+stairs[i-1])
print(dp[n])
