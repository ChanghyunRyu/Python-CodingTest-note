def solution(n):
    ternary = ternary_conversion(n)
    ternary = ternary[::-1]
    answer = decimal_conversion(ternary)
    return answer


def ternary_conversion(number):
    result = []
    while number >= 3:
        result.append(number % 3)
        number = number // 3
    result.append(number)
    return result


def decimal_conversion(ternary):
    result = 0
    for i in range(len(ternary)):
        result += ternary[i]*(3**i)
    return result


print(solution(45))
print(solution(125))
