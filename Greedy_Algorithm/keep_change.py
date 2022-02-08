import time


# 시간복잡도 계산을 위한 시간 측정
start_time = time.time()

money = 1890
coins = [500, 100, 50, 10]

num = 0
for coin in coins:
    num += int(money/coin)
    # num += money//coin
    money %= coin

print('coins: {}'.format(num))

end_time = time.time()
print('times: {}'.format(end_time-start_time))
