from itertools import permutations


def solution(ability):
    answer = 0
    case_table = list(range(len(ability)))
    sport = len(ability[0])
    for case in permutations(case_table, sport):
        temp = 0
        for i in range(sport):
            temp += ability[case[i]][i]
        answer = max(answer, temp)
    return answer
