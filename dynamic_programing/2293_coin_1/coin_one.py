n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
coins.sort()

dp = [0]*(k+1)
dp[0] = 1
for c in coins:
    for i in range(1, k+1):
        if i >= c:
            dp[i] += dp[i-c]
print(dp[-1])
