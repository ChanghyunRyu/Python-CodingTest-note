n = int(input())
sequence = list(map(int, input().split()))

dp = [0]*n
dp[0] = sequence[0]

for i in range(1, n):
    dp[i] = sequence[i]
    for j in range(i, 0, -1):
        if sequence[j-1] < sequence[i]:
            dp[i] = max(dp[i], dp[j-1]+sequence[i])

print(max(dp))
