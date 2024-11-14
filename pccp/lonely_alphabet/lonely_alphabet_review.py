def solution(input_string):
    before_letter = ''
    check = {}
    for i in range(len(input_string)):
        if before_letter != input_string[i]:
            if input_string[i] in check:
                check[input_string[i]] += 1
            else:
                check[input_string[i]] = 1
        before_letter = input_string[i]
    result = []
    for key in check:
        if check[key] > 1:
            result.append(key)
    result.sort()
    if len(result) > 0:
        return ''.join(result)
    else:
        return 'N'


print(solution("edeaaabbccd"))
print(solution("string"))
