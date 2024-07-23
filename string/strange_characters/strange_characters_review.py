def solution(s):
    answer = []
    index = 0
    for char in s:
        if char == ' ':
            answer.append(char)
            index = 0
            continue
        if index % 2 == 0:
            answer.append(char.upper())
        else:
            answer.append(char.lower())
        index += 1
    return ''.join(answer)


print(solution("try hello world"))
