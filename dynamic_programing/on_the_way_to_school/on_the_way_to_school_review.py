def solution(m, n, puddles):
    dp = [[0]*m for _ in range(n)]
    dp[0][0] = 1
    for puddle in puddles:
        dp[puddle[1]-1][puddle[0]-1] = -1
    for i in range(n):
        for j in range(m):
            if dp[i][j] == -1 or (i == 0 and j == 0):
                continue
            left = up = 0
            if j-1 >= 0 and dp[i][j-1] != -1:
                left = dp[i][j-1]
            if i-1 >= 0 and dp[i-1][j] != -1:
                up = dp[i-1][j]
            dp[i][j] = (left+up) % 1000000007
    return dp[n-1][m-1]


print(solution(4, 3, [[2, 2]]))
