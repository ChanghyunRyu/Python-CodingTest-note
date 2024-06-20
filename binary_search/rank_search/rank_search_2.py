from itertools import combinations
from collections import defaultdict
from bisect import bisect_left


def solution(info, query):
    answer = []
    applicants = info_to_dict(info)
    for q in query:
        key, score = query_to_key(q)
        pass_applicant = applicants[key]
        number = len(pass_applicant) - bisect_left(pass_applicant, score)
        answer.append(number)
    return answer


def info_to_dict(info):
    result = defaultdict(list)
    for i in info:
        tokens = i.split()
        score = int(tokens.pop())
        result[''.join(tokens)].append(score)
        for j in range(4):
            cbi = combinations(tokens, j)
            for c in cbi:
                result[''.join(c)].append(score)
    for i in result:
        result[i].sort()
    return result


def query_to_key(query):
    tokens = query.split()
    score = tokens.pop()
    key = ''.join(tokens)
    key = key.replace('and', '').replace(' ', '').replace('-', '')
    return key, int(score)


info_test = ["java backend junior pizza 150", "python frontend senior chicken 210",
             "python frontend senior chicken 150", "cpp backend senior pizza 260",
             "java backend junior chicken 80", "python backend senior chicken 50"]
query_test = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
              "cpp and - and senior and pizza 250",
              "- and backend and senior and - 150",
              "- and - and - and chicken 100",
              "- and - and - and - 150"]
print(solution(info_test, query_test))
