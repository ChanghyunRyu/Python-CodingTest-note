from collections import defaultdict
from itertools import combinations
from bisect import bisect_left


def solution(info, query):
    applicant = defaultdict(list)
    for information in info:
        data = information.split(' ')
        applicant[''].append(int(data[-1]))
        for i in range(1, 5):
            for com in combinations(data[:4], i):
                applicant[''.join(com)].append(int(data[-1]))
    for key in applicant.keys():
        applicant[key].sort()

    answer = []
    for q in query:
        data = q.split(' and ')
        temp = []
        for i in range(3):
            if data[i] == '-':
                continue
            temp.append(data[i])
        food, score = data[-1].split(' ')
        if food != '-':
            temp.append(food)
        keyword = ''.join(temp)
        answer.append(len(applicant[keyword])-bisect_left(applicant[keyword], int(score)))
    return answer


info1 = ["java backend junior pizza 150",
         "python frontend senior chicken 210",
         "python frontend senior chicken 150",
         "cpp backend senior pizza 260",
         "java backend junior chicken 80",
         "python backend senior chicken 50"]

query1 = ["java and backend and junior and pizza 100",
          "python and frontend and senior and chicken 200",
          "cpp and - and senior and pizza 250",
          "- and backend and senior and - 150",
          "- and - and - and chicken 100",
          "- and - and - and - 150"]
print(solution(info1, query1))
