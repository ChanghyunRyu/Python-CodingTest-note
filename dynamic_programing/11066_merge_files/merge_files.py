import sys
INF = int(1e9)

t = int(input())
for _ in range(t):
    k = int(sys.stdin.readline().rstrip())
    files = list(map(int, sys.stdin.readline().split()))

    pfs = [0]*(k+1)
    pfs[0] = 0
    dp = [[INF]*k for _ in range(k)]
    for i in range(k):
        pfs[i+1] = pfs[i]+files[i]
        dp[i][i] = 0

    for d in range(1, k):
        for start in range(k-d):
            end = start+d
            for mid in range(start, end):
                dp[start][end] = min(dp[start][end], dp[start][mid]+dp[mid+1][end]+pfs[end+1]-pfs[start])

    print(dp[0][k-1])
