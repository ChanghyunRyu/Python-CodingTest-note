# n,m 숫자와 카드를 입력받는다.
n, m = map(int, input().split())
card = []
for i in range(n):
    line = list(map(int, input().split()))
    card.append(line)

# 게임의 규칙에 맞게 뽑은 카드를 출력한다.
result = 0
for i in range(n):
    choice = card[i]
    choice.sort()
    if result < choice[0]:
        result = choice[0]
print(result)
