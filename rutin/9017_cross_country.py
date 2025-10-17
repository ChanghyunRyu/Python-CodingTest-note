t = int(input())
for _ in range(t):
    n = int(input())
    rate = list(map(int, input().split()))
    teams = {}
    eliminate = {}
    for i in range(len(rate)):
        if rate[i] in teams:
            teams[rate[i]].append(i)
        else:
            teams[rate[i]] = [i]
    for num in teams:
        if len(teams[num]) < 6:
            eliminate[num] = 1

    teams = {}
    count = 0
    for r in rate:
        if r in eliminate:
            continue
        count += 1
        if r in teams:
            teams[r].append(count)
        else:
            teams[r] = [count]

    min_score = 4000
    last_team = [1000]*6
    result = 0
    for num in teams:
        if num in eliminate:
            continue
        now = teams[num]
        score = now[0] + now[1] + now[2] + now[3]
        if min_score > score:
            min_score = score
            result = num
            last_team = now
        elif min_score == score:
            if last_team[4] > now[4]:
                min_score = score
                result = num
                last_team = now
    print(result)
