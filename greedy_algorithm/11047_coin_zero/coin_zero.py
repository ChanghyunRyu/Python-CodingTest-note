import sys

n, k = map(int, sys.stdin.readline().split())
coins = []
for _ in range(n):
    coins.append(int(sys.stdin.readline().rstrip()))

change = k
count = 0
i = len(coins)-1
while change > 0:
    if change < coins[i]:
        i -= 1
        continue
    quo = change//coins[i]
    change %= coins[i]
    count += quo
print(count)
