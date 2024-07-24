def solution(s):
    answer = len(s)
    for i in range(1, len(s)//2+1):
        tmp_length = compress_string(s, i)
        if answer > tmp_length:
            answer = tmp_length
    return answer


def compress_string(s, interval):
    temp = []
    before_token = s[:interval]
    count = 1
    for i in range(interval, len(s), interval):
        end = i+interval
        if i+interval >= len(s):
            end = len(s)

        if before_token == s[i:end]:
            count += 1
        else:
            if count == 1:
                temp.append(before_token)
            else:
                temp.append('{}{}'.format(count, before_token))
            before_token = s[i:end]
            count = 1
    if count == 1:
        temp.append(before_token)
    else:
        temp.append('{}{}'.format(count, before_token))
    s = ''.join(temp)
    return len(s)


print(solution('aabbaccc'))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcabcabcdededededede"))
