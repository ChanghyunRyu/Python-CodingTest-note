from itertools import combinations
from bisect import bisect_left


def solution(info, query):
    result = []
    dictionary = info_to_dict(info)
    for q in query:
        temp = get_successful_candidates(q, dictionary)
        result.append(temp)
    return result


def info_to_dict(info):
    result = {}
    for applicant in info:
        tokens = applicant.split()
        insert_token_dict(tokens, result)
    for key in result:
        result[key].sort()
    return result


def insert_token_dict(tokens, dictionary):
    score = int(tokens[4])
    tokens = tokens[:4]
    for i in range(len(tokens)+1):
        for combination in combinations(tokens, i):
            key = ''.join(combination)
            if key in dictionary:
                dictionary[key].append(score)
            else:
                dictionary[key] = [score]


def get_successful_candidates(query, dictionary):
    tokens = query.split()
    score = int(tokens[len(tokens)-1])
    tokens = tokens[:len(tokens)-1]
    temp = []
    for token in tokens:
        if token == '-' or token == 'and':
            continue
        else:
            temp.append(token)
    final_query = ''.join(temp)
    if final_query in dictionary:
        applicants = dictionary[final_query]
        result = len(applicants) - bisect_left(applicants, score)
    else:
        result = 0
    return result


info_example = ["java backend junior pizza 150",
                "python frontend senior chicken 210",
                "python frontend senior chicken 150",
                "cpp backend senior pizza 260",
                "java backend junior chicken 80",
                "python backend senior chicken 50"]

query_example = ["java and backend and junior and pizza 100",
                 "python and frontend and senior and chicken 200",
                 "cpp and - and senior and pizza 250",
                 "- and backend and senior and - 150",
                 "- and - and - and chicken 100",
                 "- and - and - and - 150"]
print(solution(info_example, query_example))
