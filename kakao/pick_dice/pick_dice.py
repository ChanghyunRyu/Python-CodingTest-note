from itertools import combinations
from bisect import bisect_left


def solution(dice):
    answer = []
    dp = {}
    max_win = 0
    for combination in combinations(list(range(1, len(dice)+1)), len(dice)//2):
        if combination not in dp:
            temp = []
            get_dice_sum(0, 0, combination, dice, temp)
            temp.sort()
            dp[combination] = temp
        a = dp[combination]
        a_side = set(combination)
        all_side = set(range(1, len(dice)+1))
        b_side = tuple(all_side-a_side)
        if b_side not in dp:
            temp = []
            get_dice_sum(0, 0, b_side, dice, temp)
            temp.sort()
            dp[b_side] = temp
        b = dp[b_side]
        wins = get_win(a, b)
        if max_win < wins:
            max_win = wins
            answer = list(combination)
    return answer


def get_dice_sum(i, score, index, dice, result):
    if i >= len(index):
        result.append(score)
    else:
        for num in dice[index[i]-1]:
            get_dice_sum(i+1, score+num, index, dice, result)


def get_win(a, b):
    result = 0
    for num in a:
        result += bisect_left(b, num)
    return result


d1 = [[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]]
d2 = [[1, 2, 3, 4, 5, 6], [2, 2, 4, 4, 6, 6]]
d3 = [[40, 41, 42, 43, 44, 45], [43, 43, 42, 42, 41, 41], [1, 1, 80, 80, 80, 80], [70, 70, 1, 1, 70, 70]]
print(solution(d1))
print(solution(d2))
print(solution(d3))
