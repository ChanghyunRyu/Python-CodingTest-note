def solution(s):
    answer = []
    tmp_sets = str_to_set(s)
    tmp_sets = sorted(tmp_sets, key=lambda x: len(x))
    before_set = set()
    for now_set in tmp_sets:
        answer.append(list(now_set-before_set)[0])
        before_set = now_set
    return answer


def str_to_set(string):
    result = []
    in_set = False
    num_tmp = []
    tmp_set = set()
    for i in range(1, len(string)-1):
        if string[i] == '{':
            tmp_set = set()
            in_set = True
        if string[i] == '}':
            tmp_set.add(int(''.join(num_tmp)))
            num_tmp = []
            result.append(tmp_set)
            in_set = False
        if in_set:
            if string[i].isdigit():
                num_tmp.append(string[i])
            elif string[i] == ',':
                tmp_set.add(int(''.join(num_tmp)))
                num_tmp = []
    return result


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
