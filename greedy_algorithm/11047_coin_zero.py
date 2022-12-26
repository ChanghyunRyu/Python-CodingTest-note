#백준 11047번 문제 동전 0
n, k = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(input()))

coins.sort(reverse=True)
count = 0
index = 0
# 처음 디자인 당시, 그냥 동전 금액만큼 빼주는 작업만 했음! 이럴 경우, 문제에 기재되어 있는 제한시간이 오바됨!
# 문제 조건과 변수의 범위를 잘 살필 것!
while True:
    if k == 0 or index >= n:
        break
    coin_num = k//coins[index]
    if coin_num > 0:
        k -= coins[index]*coin_num
        count += coin_num
    else:
        index += 1
print(count)
