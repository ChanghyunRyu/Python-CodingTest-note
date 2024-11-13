from itertools import combinations


def get_max_honey(honeycomb, c):
    result = 0
    for i in range(1, len(honeycomb)+1):
        for choice in combinations(honeycomb, i):
            answer = 0
            if sum(choice) > c:
                continue
            for honey in choice:
                answer += honey**2
            result = max(result, answer)
    return result


T = int(input())
for test_case in range(1, T + 1):
    N, M, C = map(int, input().split())
    hive = []
    for _ in range(N):
        hive.append(list(map(int, input().split())))
    case_table =[]
    for i in range(N):
        for j in range(N-M+1):
            case_table.append((i, j))
    answer = 0
    for p1, p2 in combinations(case_table, 2):
        if p1[0] == p2[0] and p1[1]+M > p2[1]:
            continue
        h1 = []
        h2 = []
        for i in range(M):
            h1.append(hive[p1[0]][p1[1]+i])
            h2.append(hive[p2[0]][p2[1]+i])
        temp = get_max_honey(h1, C) + get_max_honey(h2, C)
        answer = max(answer, temp)
    print('#{} {}'.format(test_case, answer))
