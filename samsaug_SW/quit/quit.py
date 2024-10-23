n = int(input())
counsel = []
for i in range(1, n+1):
    day, amount = map(int, input().split())
    counsel.append((i, i+day, amount))

dp = [0]*(n+2)
for day in range(1, n+2):
    temp = 0
    for i in range(len(counsel)):
        start, end, amount = counsel[i]
        if end == day:
            temp = max(temp, max(dp[:start+1])+amount)
    dp[day] = temp

print(max(dp))
