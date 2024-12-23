def solution(friends, gifts):
    answer = 0
    check_gift = {}
    score = {}
    for friend in friends:
        check_gift[friend] = dict()
        for other in friends:
            if other == friend:
                continue
            check_gift[friend][other] = 0
        score[friend] = 0

    for gift in gifts:
        giver, receiver = gift.split()
        if receiver in check_gift[giver]:
            check_gift[giver][receiver] += 1
        score[giver] += 1
        score[receiver] -= 1

    for friend in friends:
        temp = 0
        for other in check_gift[friend]:
            if check_gift[friend][other] > check_gift[other][friend]:
                temp += 1
            elif check_gift[friend][other] == check_gift[other][friend] and score[friend] > score[other]:
                temp += 1
        answer = max(answer, temp)
    return answer


f1 = ["muzi", "ryan", "frodo", "neo"]
g1 = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]
print(solution(f1, g1))
