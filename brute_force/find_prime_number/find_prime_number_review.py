import itertools


def solution(numbers):
    answer = set()
    for i in range(1, len(numbers)+1):
        for permutation in itertools.permutations(numbers, i):
            permutation = list(permutation)
            number = int(''.join(permutation))
            if get_prime_numbers(number):
                answer.add(number)
    return len(answer)


def get_prime_numbers(number):
    m = int(number**0.5)
    if number == 0 or number == 1:
        return False
    for i in range(2, m+1):
        if number % i == 0:
            return False
    return True


print(solution('011'))
