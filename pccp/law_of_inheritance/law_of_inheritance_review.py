inheritance = {'Rr': ['RR', 'Rr', 'Rr', 'rr'],
               'RR': ['RR', 'RR', 'RR', 'RR'],
               'rr': ['rr', 'rr', 'rr', 'rr']}


def get_answer(query):
    generation, sequence = query
    if generation == 1:
        return 'Rr'
    p_generation = generation-1
    p_sequence, idx = divmod(sequence-1, 4)
    return inheritance[get_answer([p_generation, p_sequence])][idx]


def solution(queries):
    answer = []
    for q in queries:
        answer.append(get_answer(q))
    return answer
