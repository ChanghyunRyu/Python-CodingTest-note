dp = [0]*31
dp[0] = 1
dp[2] = 3
for i in range(4, 31):
    if i % 2 == 1:
        continue

    result = 2
    num = 3
    for j in range(i-2, 0, -2):
        result += dp[j]*num
        num = 2
    dp[i] = result

n = int(input())
print(dp[n])
