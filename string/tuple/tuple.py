def solution(s):
    answer = []
    tmp = [0]*501
    tmp[0] = set([])
    in_set = False
    for i in range(1, len(s)-1):
        if s[i] == '{':
            start = i+1
            tmp_set = set()
            in_set = True
        elif in_set and s[i] == ',':
            tmp_set.add(int(s[start:i]))
            start = i+1
        elif s[i] == '}':
            in_set = False
            tmp_set.add(int(s[start:i]))
            tmp[len(tmp_set)] = tmp_set
    for i in range(1, len(tmp)):
        if tmp[i] == 0:
            break
        answer.append(list(tmp[i]-tmp[i-1])[0])
    return answer


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
