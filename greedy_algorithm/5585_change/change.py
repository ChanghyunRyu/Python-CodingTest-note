money = 1000 - int(input())
coins = [500, 100, 50, 10, 5, 1]
i = 0
result = 0
while money > 0:
    if money < coins[i]:
        i += 1
        continue
    else:
        result += money//coins[i]
        money %= coins[i]
print(result)
