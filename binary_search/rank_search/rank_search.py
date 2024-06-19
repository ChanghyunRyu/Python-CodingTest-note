from itertools import combinations
from collections import defaultdict
from bisect import bisect_left


def solution(info, query):
    answer = []
    applicants = info_to_applicant(info)
    for q in query:
        key = q.split()
        score = int(key.pop())
        key = ''.join(key)
        key = key.replace('and', '').replace(' ', '').replace('-', '')
        pass_applicants = applicants[key]

        result = len(pass_applicants) - bisect_left(pass_applicants, score)
        answer.append(result)
    return answer


def info_to_applicant(info):
    applicant = defaultdict(list)
    for i in info:
        person = i.split()
        score = int(person.pop())
        applicant[''.join(person)].append(score)

        for j in range(4):
            candi = list(combinations(person, j))
            for c in candi:
                applicant[''.join(c)].append(score)
    for i in applicant:
        applicant[i].sort()
    return applicant


info_test = ["java backend junior pizza 150", "python frontend senior chicken 210",
             "python frontend senior chicken 150", "cpp backend senior pizza 260",
             "java backend junior chicken 80", "python backend senior chicken 50"]
query_test = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
              "cpp and - and senior and pizza 250",
              "- and backend and senior and - 150",
              "- and - and - and chicken 100",
              "- and - and - and - 150"]
print(solution(info_test, query_test))
