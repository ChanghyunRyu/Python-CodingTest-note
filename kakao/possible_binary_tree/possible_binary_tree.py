def solution(numbers):
    answer = []
    check = []
    for i in range(1, 7):
        check.append(2**i-1)

    for number in numbers:
        ten_num = ten_to_binary(number)
        if check_binary(ten_num, check):
            answer.append(1)
        else:
            answer.append(0)
    return answer


def ten_to_binary(number):
    result = []
    while number >= 2:
        number, remain = divmod(number, 2)
        result.append(remain)
    else:
        result.append(number)
    return result[::-1]


def check_binary(number, check):
    for c in check:
        if len(number) == c:
            break
        elif len(number) < c:
            number = [0]*(c-len(number)) + number
            break
    if len(number) == 1:
        return True

    mid = (len(number)-1)//2
    if number[mid] == 0 and sum(number) > 0:
        return False
    if check_binary(number[:mid], [mid]) and check_binary(number[mid+1:], [mid]):
        return True


print(solution([7, 42, 5]))
print(solution([63, 111, 95]))
