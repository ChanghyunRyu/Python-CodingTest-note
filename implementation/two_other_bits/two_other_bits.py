def solution(numbers):
    answer = []
    for n in numbers:
        answer.append(find_2bits(n))
    return answer


def find_2bits(number):
    bits_number = ten_to_two(number)
    result = bits_number
    if bits_number[0] == 0:
        result[0] = 1
        return two_to_ten(result)
    for i in range(1, len(bits_number)):
        if bits_number[i] == 0 and bits_number[i-1] == 1:
            result[i] = 1
            result[i-1] = 0
            return two_to_ten(result)


def ten_to_two(number):
    result = []
    while number >= 2:
        result.append(number % 2)
        number = number//2
    result.append(number)
    result.append(0)
    return result


def two_to_ten(number):
    result = 0
    for i in range(len(number)):
        result += number[i]*(2**i)
    return result


print(ten_to_two(179))
print(solution([2, 7]))
print(solution([15, 127, 179, 3783, 819199, 9126805503, 38588121087, 8796093022207, 17592186044415]))
