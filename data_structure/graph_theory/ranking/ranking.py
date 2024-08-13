def solution(n, results):
    rank = {}
    for i in range(1, n+1):
        rank[i] = [set(), set()]
    for result in results:
        winner, loser = result
        rank[winner][0].add(loser)
        rank[loser][1].add(winner)
    flag = True
    while flag:
        flag = False
        for player in rank:
            # losers = 플레이어가 이긴 사람들, winners = 플레이어가 진 사람들
            losers, winners = rank[player]
            new_losers = set(losers)
            for loser in losers:
                for loser_loser in rank[loser][0]:
                    new_losers.add(loser_loser)
            new_winners = set(winners)
            for winner in winners:
                for winner_winner in rank[winner][1]:
                    new_winners.add(winner_winner)
            if len(losers)+len(winners) != len(new_losers)+len(new_winners):
                flag = True
            rank[player] = [new_losers, new_winners]

    answer = 0
    for player in rank:
        losers, winners = rank[player]
        if len(losers)+len(winners) >= n-1:
            answer += 1
    return answer


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
