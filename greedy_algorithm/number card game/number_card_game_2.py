n, m = map(int, input().split())
card = []
for i in range(n):
    line = list(map(int, input().split()))
    card.append(line)

result = 0
for i in range(n):
    choice = card[i]
    choice.sort()
    if result < choice[0]:
        result = choice[0]
print(result)
