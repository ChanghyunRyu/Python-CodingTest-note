def solution(s):
    flag = True
    answer = [0, 0]
    while flag:
        number, zeros = delete_zeros(s)
        answer[0] += 1
        answer[1] += zeros
        s = binary_conversion(number)
        if s == '1':
            flag = False
    return answer


def delete_zeros(s):
    count = 0
    for character in s:
        if character == '1':
            count += 1
    return count, len(s)-count


def binary_conversion(number):
    temp = []
    while number >= 2:
        temp.append(str(number % 2))
        number = number // 2
    temp.append(str(number))
    return ''.join(temp[::-1])


print(solution("110010101001"))
