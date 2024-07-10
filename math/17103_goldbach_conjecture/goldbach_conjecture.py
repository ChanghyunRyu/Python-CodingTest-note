import sys


def return_prime_number(number):
    is_prime = [True]*number
    is_prime[1] = False
    end = int(number**0.5)
    for i in range(2, end+1):
        if is_prime[i]:
            for j in range(i+i, number, i):
                is_prime[j] = False
    return [i for i in range(2, number) if is_prime[i]]


def find_goldbach_partition(number, prime):
    prime_numbers = prime
    start, end = 0, len(prime_numbers)-1
    answer = 0
    while start <= end:
        cal = prime_numbers[start]+prime_numbers[end]
        if cal == number:
            answer += 1
            start += 1
        elif cal > number:
            end -= 1
        elif cal < number:
            start += 1
    return answer


t = int(input())
prime_number = return_prime_number(1000000)
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    partitions = find_goldbach_partition(n, prime_number)
    print(partitions)
