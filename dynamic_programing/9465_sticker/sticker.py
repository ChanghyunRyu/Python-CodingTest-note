t = int(input())
for _ in range(t):
    n = int(input())
    sticker = []
    for _ in range(2):
        sticker.append(list(map(int, input().split())))

    dp = [[0]*(n+1) for _ in range(2)]
    dp[0][1] = sticker[0][0]
    dp[1][1] = sticker[1][0]
    for i in range(2, n+1):
        dp[0][i] = sticker[0][i-1] + max(dp[1][i-1], dp[0][i-2], dp[1][i-2])
        dp[1][i] = sticker[1][i-1] + max(dp[0][i-1], dp[0][i-2], dp[1][i-2])

    print(max(dp[0][-1], dp[0][-2], dp[1][-1], dp[1][-2]))
