def solution(s):
    answer = []
    count = 0
    zero = 0
    while s != "1" and count < 5:
        count += 1
        tmp = []
        for char in s:
            if char == '1':
                tmp.append(char)
        zero += len(s)-len(tmp)
        s = str(format(len(tmp), 'b'))
    answer.append(count)
    answer.append(zero)
    return answer


print(solution("110010101001"))
