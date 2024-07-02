## 순위

---

[출처] https://school.programmers.co.kr/learn/courses/30/lessons/49191

n명의 권투선수가 권투 대회에 참여했고 각각 1번부터 n번까지 번호를 받았습니다. 
권투 경기는 1대1 방식으로 진행이 되고, 
만약 A 선수가 B 선수보다 실력이 좋다면 A 선수는 B 선수를 항상 이깁니다. 
심판은 주어진 경기 결과를 가지고 선수들의 순위를 매기려 합니다. 
하지만 몇몇 경기 결과를 분실하여 정확하게 순위를 매길 수 없습니다.

선수의 수 n, 경기 결과를 담은 2차원 배열 results가 매개변수로 주어질 때 
정확하게 순위를 매길 수 있는 선수의 수를 return 하도록 solution 함수를 작성해주세요.

### 제한 사항

- 선수의 수는 1명 이상 100명 이하입니다.
- 경기 결과는 1개 이상 4,500개 이하입니다.
- results 배열 각 행 [A, B]는 A 선수가 B 선수를 이겼다는 의미입니다.
- 모든 경기 결과에는 모순이 없습니다.

---
### Problem Solved Check
- [x] 1회  24/07/02
- [ ] 2회
- [ ] 3회

그래프를 사용하지 않는 방법이 먼저 떠올라서 해당 방법으로 먼저 풀어보았다.
~~~
def solution(n, results):
    ranking = {}
    for i in range(1, n+1):
        ranking[i] = [set(), set()]
    for winner, loser in results:
        ranking[winner][1].add(loser)
        ranking[loser][0].add(winner)
    is_update = True
    while is_update:
        ranking, is_update = update_ranking(ranking)
    answer = 0
    for player in ranking:
        winners, losers = ranking[player]
        if len(winners)+len(losers) == n-1:
            answer += 1
    return answer


def update_ranking(ranking):
    is_update = False
    for player in ranking:
        # winners = 나한테 이긴 선수, losers = 나한테 진 선수
        winners, losers = ranking[player]
        new_winners = set(winners)
        for win in winners:
            for i in ranking[win][0]:
                new_winners.add(i)
        ranking[player][0] = new_winners
        if len(new_winners) != len(winners):
            is_update = True

        new_losers = set(losers)
        for lose in losers:
            for i in ranking[lose][1]:
                new_losers.add(i)
        ranking[player][1] = new_losers
        if len(new_losers) != len(losers):
            is_update = True
    return ranking, is_update
    
~~~
플로이드-워셜 알고리즘을 사용한 그래프 풀이는 다음과 같다.
~~~
def solution(n, results):
    graph = [[0]*n for _ in range(n)]
    for i in range(n):
        graph[i][i] = 'self'
    for winner, loser in results:
        graph[winner-1][loser-1] = 'win'
        graph[loser-1][winner-1] = 'lose'
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] == 'win' and graph[k][j] == 'win':
                    graph[i][j] = 'win'
                if graph[i][k] == 'lose' and graph[k][j] == 'lose':
                    graph[i][j] = 'lose'
    answer = 0
    for g in graph:
        if 0 not in g:
            answer += 1
    return answer
    
~~~