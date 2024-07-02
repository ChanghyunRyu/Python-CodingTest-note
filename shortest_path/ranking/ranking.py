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


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
