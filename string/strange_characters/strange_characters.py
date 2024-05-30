def solution(s):
    answer = ''
    index = 0
    for ch in s:
        if ch == ' ':
            answer = ''.join([answer, ch])
            index = 0
            continue
        if index % 2 == 0:
            answer = ''.join([answer, ch.upper()])
        else:
            answer = ''.join([answer, ch.lower()])
        index += 1
    return answer


print(solution("try hello world"))
