def solution(participant, completion):
    complete = {}
    for person in completion:
        if person in complete:
            complete[person] += 1
        else:
            complete[person] = 1

    for person in participant:
        if person in complete and complete[person] > 0:
            complete[person] -= 1
            continue
        else:
            answer = person
            break
    return answer
