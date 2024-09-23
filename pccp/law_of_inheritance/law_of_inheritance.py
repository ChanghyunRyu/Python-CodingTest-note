def solution(queries):
    answer = []
    law = {'RR': ['RR', 'RR', 'RR', 'RR'],
           'Rr': ['RR', 'Rr', 'Rr', 'rr'],
           'rr': ['rr', 'rr', 'rr', 'rr']}
    for g, n in queries:
        answer.append(return_characteristics(g, n, law))
    return answer


def return_characteristics(generation, number, law):
    if generation == 1:
        return 'Rr'
    number, remain = divmod(number-1, 4)
    parent = return_characteristics(generation-1, number+1, law)
    return law[parent][remain]


print(solution([[3, 5]]))
print(solution([[3, 8], [2, 2]]))
print(solution([[3, 1], [2, 3], [3, 9]]))
print(solution([[4, 26]]))
