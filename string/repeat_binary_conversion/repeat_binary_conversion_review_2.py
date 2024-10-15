def solution(s):
    zero = count = 0
    while s != '1':
        count += 1
        ones = 0
        for i in range(len(s)):
            if s[i] == '0':
                zero += 1
            else:
                ones += 1
        s = number_to_binary(ones)
    return [count, zero]


def number_to_binary(num):
    binary = []
    while num != 0:
        num, remain = divmod(num, 2)
        binary.append(str(remain))
    return ''.join(binary[::-1])


print(solution("110010101001"))
print(solution("01110"))
print(solution('1111111'))
