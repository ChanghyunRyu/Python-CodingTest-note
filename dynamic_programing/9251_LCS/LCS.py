txt1 = input()
txt2 = input()

dp = [[0]*(len(txt1)+1) for _ in range(len(txt2)+1)]
for i in range(1, len(txt1)+1):
    for j in range(1, len(txt2)+1):
        if txt1[i-1] == txt2[j-1]:
            dp[j][i] = dp[j-1][i-1]+1
        else:
            dp[j][i] = max(dp[j-1][i], dp[j][i-1])
print(dp[len(txt2)][len(txt1)])
