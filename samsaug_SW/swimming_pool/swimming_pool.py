T = int(input())

for test_case in range(1, T + 1):
    day, month, month_3, year = map(int, input().split())
    plan = list(map(int, input().split()))
    dp = [0]*13
    for i in range(1, 13):
        dp[i] = dp[i-1]+min(day*plan[i-1], month)
        if i > 2:
            dp[i] = min(dp[i-3]+month_3, dp[i])
    answer = min(year, dp[12])
    print('#{} {}'.format(test_case, answer))