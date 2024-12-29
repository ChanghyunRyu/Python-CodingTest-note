def solution(survey, choices):
    answer = []
    personality = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    for i in range(len(choices)):
        p1, p2 = survey[i]
        choice = choices[i]
        if choice <= 3:
            personality[p1] += 4-choice
        elif choice >= 5:
            personality[p2] += choice-4
    order = ['RT', 'CF', 'JM', 'AN']
    for i in range(len(order)):
        o1, o2 = order[i]
        if personality[o1] >= personality[o2]:
            answer.append(o1)
        else:
            answer.append(o2)
    return ''.join(answer)


s1 = ["AN", "CF", "MJ", "RT", "NA"]
c1 = [5, 3, 2, 7, 5]
print(solution(s1, c1))
