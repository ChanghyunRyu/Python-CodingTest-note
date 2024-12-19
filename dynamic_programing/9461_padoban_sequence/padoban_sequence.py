t = int(input())
dp = [1]*100
for i in range(3, 100):
    dp[i] = dp[i-2]+dp[i-3]
for _ in range(t):
    n = int(input())
    print(dp[n-1])
