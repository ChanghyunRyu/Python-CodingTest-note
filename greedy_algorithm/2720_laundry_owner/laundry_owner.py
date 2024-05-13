import sys

t = int(input())
coins = [25, 10, 5, 1]
for _ in range(t):
    change = int(sys.stdin.readline().rstrip())
    i = 0
    result = [0]*4
    while change > 0:
        if change < coins[i]:
            i += 1
            continue
        else:
            result[i] += change//coins[i]
            change %= coins[i]
    for r in result:
        print(r, end=' ')
    print()
