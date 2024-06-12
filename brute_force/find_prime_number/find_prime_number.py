import itertools


def solution(numbers):
    answer = set()
    temp = []
    for n in numbers:
        temp.append(int(n))
    numbers = temp
    for i in range(1, len(numbers)+1):
        npi = list(itertools.permutations(numbers, i))
        for np in npi:
            np = list(np)
            if np[0] == 0:
                continue
            if len(np) == 1:
                num = np[0]
            else:
                num = int(''.join(list(map(str, np))))
            if num not in answer and chk_prime_number(num):
                answer.add(num)
    return len(answer)


def chk_prime_number(n):
    if n == 1:
        return False
    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    return True


print(solution("17"))
print(solution("011"))
