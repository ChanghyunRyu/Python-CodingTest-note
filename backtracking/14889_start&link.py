import sys
n = int(input())
s = [[0]*n for i in range(n)]
for i in range(n):
    nums = list(map(int, sys.stdin.readline().split()))
    s[i] = nums
answer = 1e9


def getAnswer(idx, team, last):
    global answer, n, s
    # 팀을 3명 정하면 결과를 계산
    people = set(range(n))
    if idx == int(n/2):
        result1 = 0
        result2 = 0
        for i in team:
            temp = team - {i}
            for j in temp:
                result1 += s[i][j]
        team2 = people - team
        for i in team2:
            temp = team2 - {i}
            for j in temp:
                result2 += s[i][j]
        answer = min(abs(result1-result2), answer)
    else:
        preparations = people - team
        for person in preparations:
            if person > last:
                new_team = set(team)
                new_team.add(person)
                getAnswer(idx+1, new_team, person)


getAnswer(0, set(), -1)
print(answer)
