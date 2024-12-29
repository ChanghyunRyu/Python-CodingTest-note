def solution(n, k):
    answer = 0
    for num in convert_k(n, k).split('0'):
        if num == '':
            continue
        if check_prime_number(num):
            answer += 1
    return answer


def convert_k(number, k):
    result = []
    while number >= k:
        number, remain = divmod(number, k)
        result.append(str(remain))
    else:
        result.append(str(number))
    return ''.join(result[::-1])


def check_prime_number(number):
    number = int(number)
    if number < 2:
        return False
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True


print(solution(437674, 3))
