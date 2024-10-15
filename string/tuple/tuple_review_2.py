def solution(s):
    answer = []
    sets = string_to_set(s[1:len(s)-1])
    sets.sort(key=len)
    before_set = set()
    for s in sets:
        new_int = s-before_set
        answer.append(list(new_int)[0])
        before_set = s
    return answer


def string_to_set(s):
    result = []
    is_set = False
    for i in range(len(s)):
        if s[i] == '{':
            temp = set()
            start = i+1
            is_set = True
        elif s[i] == '}':
            temp.add(int(s[start:i]))
            result.append(temp)
            is_set = False
        elif is_set and s[i] == ',':
            temp.add(int(s[start:i]))
            start = i+1
    return result


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
