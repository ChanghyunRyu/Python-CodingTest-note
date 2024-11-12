from collections import deque


def get_distance(p, s):
    return abs(p[0] - s[0]) + abs(p[1] - s[1])


def get_time(value, p):
    processing = deque()
    while p:
        now = p.pop()
        if len(processing) < 3:
            processing.append(now+value)
        else:
            recent = processing.popleft()
            now = max(now, recent)
            processing.append(now+value)
    if processing:
        return max(list(processing))
    else:
        return 0


def get_result(p, s, case):
    stair0 = []
    stair1 = []
    for i in range(len(p)):
        if case[i] == 0:
            dist = get_distance(p[i], s[0])+1
            stair0.append(dist)
        else:
            dist = get_distance(p[i], s[1])+1
            stair1.append(dist)
        stair0.sort(reverse=True)
        stair1.sort(reverse=True)
    return max(get_time(s[0][2], stair0), get_time(s[1][2], stair1))


def make_case(p_len, case, result):
    if len(case) == p_len:
        result.append(case)
        return
    make_case(p_len, list(case)+[0], result)
    make_case(p_len, list(case)+[1], result)


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    room = []
    for _ in range(n):
        room.append(list(map(int, input().split())))
    person = []
    stairs = []
    for i in range(n):
        for j in range(n):
            if room[i][j] == 1:
                person.append((i, j))
            elif room[i][j] > 1:
                stairs.append((i, j, room[i][j]))
    cases = []
    make_case(len(person), [], cases)
    answer = int(1e9)
    for c in cases:
        answer = min(answer, get_result(person, stairs, c))
    print('#{} {}'.format(test_case, answer))
