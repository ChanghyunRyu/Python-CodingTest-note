def get_home(x, y):
    home = [0] * (2 * N)
    for i in range(N):
        for j in range(N):
            if city[i][j] == 1:
                dist = abs(x - i) + abs(y - j) + 1
                home[dist] += 1
    return home


def calc_cost(k):
    return k ** 2 + (k - 1) ** 2


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    city = []
    for _ in range(N):
        city.append(list(map(int, input().split())))

    answer = 0
    for i in range(N):
        for j in range(N):
            now_home = get_home(i, j)
            homes = 0
            for d in range(1, 2 * N):
                cost = calc_cost(d)
                homes += now_home[d]
                if homes * M - cost >= 0:
                    answer = max(answer, homes)
    print('#{} {}'.format(test_case, answer))
