import re


def solution(n, k):
    answer = 0
    k_number = conversion_k(n, k)
    for num in re.split('0+', k_number):
        if not num:
            continue
        if check_prime_number(int(num)):
            answer += 1
    return answer


def conversion_k(number, k):
    result = []
    while number >= k:
        result.append(str(number % k))
        number = number // k
    result.append(str(number))
    return ''.join(result[::-1])


def check_prime_number(number):
    if number == 0 or number == 1:
        return False
    for i in range(2, int(number*0.5)+1):
        if number % i == 0:
            return False
    return True


print(solution(437674, 3))
print(solution(110011, 10))
print(check_prime_number(2))
