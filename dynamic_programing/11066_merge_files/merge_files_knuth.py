import sys
INF = int(1e9)

t = int(input())
for _ in range(t):
    k = int(sys.stdin.readline().rstrip())
    files = list(map(int, sys.stdin.readline().split()))

    pfs = [0]*(k+1)
    num = [[0]*k for _ in range(k)]
    dp = [[0]*k for _ in range(k)]
    for i in range(k):
        num[i][i] = i
        pfs[i+1] = pfs[i]+files[i]

    for d in range(1, k):
        for start in range(k-d):
            end = start+d
            dp[start][end] = INF
            for mid in range(num[start][end-1], min(num[start+1][end]+1, end)):
                cost = dp[start][mid]+dp[mid+1][end]+pfs[end+1]-pfs[start]
                if dp[start][end] > cost:
                    dp[start][end] = cost
                    num[start][end] = mid

    print(dp[0][k-1])
