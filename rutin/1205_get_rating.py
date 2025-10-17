n, new_score, p = map(int, input().split())
if n == 0:
    print(1)
else:
    scores = list(map(int, input().split()))
    rate = 1
    count = 0
    for score in scores:
        if score > new_score:
            rate += 1
            count += 1
        elif score == new_score:
            count += 1
    if count >= p:
        print(-1)
    else:
        print(rate)
