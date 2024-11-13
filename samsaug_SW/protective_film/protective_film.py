from itertools import combinations
import copy


def shock_test(f, k, ones, zeros):
    result = True
    for y in range(len(f[0])):
        flag = False
        before_num = -1
        cnt = 0
        for i in range(len(f)):
            now = f[i][y]
            if i in ones:
                now = 1
            elif i in zeros:
                now = 0
            if now != before_num:
                before_num = now
                cnt = 1
                if cnt == k:
                    flag = True
                    break
            else:
                cnt += 1
                if cnt == k:
                    flag = True
                    break
        if not flag:
            result = False
            break
    return result


T = int(input())
for test_case in range(1, T + 1):
    D, W, K = map(int, input().split())
    film = []
    for _ in range(D):
        film.append(list(map(int, input().split())))
    answer = 0
    all_ones = [1]*W
    all_zeros = [0]*W
    case_table = list(range(D))
    while answer < K:
        flag = False
        if answer > 0:
            for choice in combinations(case_table, answer):
                if shock_test(film, K, [], choice):
                    flag = True
                    break
                for i in range(1, len(choice)+1):
                    for com in combinations(choice, i):
                        if shock_test(film, K, com, choice):
                            flag = True
                            break
            if flag:
                break
        elif shock_test(film, K, [], []):
            break
        answer += 1
    print('#{} {}'.format(test_case, answer))
