def solution(input_string):
    answer = []
    before_char = input_string[0]
    record = { before_char: 1}
    for i in range(1, len(input_string)):
        if before_char == input_string[i]:
            continue
        else:
            if input_string[i] in record:
                record[input_string[i]] += 1
            else:
                record[input_string[i]] = 1
            before_char = input_string[i]

    for character in record:
        if record[character] >= 2:
            answer.append(character)
    answer.sort()
    answer = ''.join(answer)
    if answer == '':
        answer = 'N'
    return answer


print(solution("edeaaabbccd"))
print(solution("eeddee"))
print(solution("string"))
print(solution("zbzbz"))
