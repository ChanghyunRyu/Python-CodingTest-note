def solution(participant, completion):
    pass_participant = {}
    for c in completion:
        if c not in pass_participant:
            pass_participant[c] = 1
        else:
            pass_participant[c] += 1
    for p in participant:
        if p not in pass_participant:
            return p
        else:
            pass_participant[p] -= 1
            if pass_participant[p] < 0:
                return p


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
