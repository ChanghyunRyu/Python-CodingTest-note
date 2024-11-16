T = int(input())
for test_case in range(1, T + 1):
    N, L = map(int, input().split())
    foods = []
    for _ in range(N):
        foods.append(list(map(int, input().split())))

    dp = [[0] * (L + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        score, kcal = foods[i - 1]
        for w in range(1, L + 1):
            if w < kcal:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(dp[i - 1][w - kcal] + score, dp[i - 1][w])
    answer = dp[N][L]
    print('#{} {}'.format(test_case, answer))
