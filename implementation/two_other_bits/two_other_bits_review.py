def solution(numbers):
    answer = []
    for n in numbers:
        answer.append(find_2bits(n))
    return answer


def find_2bits(number):
    two_bits = ten_to_two(number)
    before_bits = two_bits[0]
    if before_bits == 0:
        two_bits[0] = 1
        return two_to_ten(two_bits)
    for i in range(1, len(two_bits)):
        if two_bits[i] == 0 and before_bits == 1:
            two_bits[i] = 1
            two_bits[i-1] = 0
            break
        before_bits = two_bits[i]
    return two_to_ten(two_bits)


def ten_to_two(number):
    result = []
    while number >= 2:
        number, mod = divmod(number, 2)
        result.append(mod)
    result.append(number)
    result.append(0)
    return result


def two_to_ten(numbers):
    result = 0
    for i in range(len(numbers)):
        result += 2**i*numbers[i]
    return result


print(solution([4321, 11, 5, 27, 75]))
