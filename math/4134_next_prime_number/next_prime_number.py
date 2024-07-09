test = int(input())


def find_next_prime(number):
    answer = number
    while not check_prime_number(answer):
        answer += 1
    return answer


def check_prime_number(number):
    if number == 1 or number == 0:
        return False
    end = int(number**0.5)
    for i in range(2, end+1):
        if number % i == 0:
            return False
    return True


for _ in range(test):
    n = int(input())
    next_prime = find_next_prime(n)
    print(next_prime)
