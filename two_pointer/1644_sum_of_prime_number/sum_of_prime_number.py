n = int(input())


def find_prefix_sum(number):
    prefix_sum = [0]
    prime_list = return_prime_list(number)
    for prime_number in prime_list:
        prefix_sum.append(prefix_sum[-1]+prime_number)
    return prefix_sum


def return_prime_list(number):
    sieve = [True]*(number+1)
    m = int((number+1)**0.5)
    for i in range(2, m+1):
        if sieve[i] is True:
            for j in range(i+i, number+1, i):
                sieve[j] = False
    return [i for i in range(2, number+1) if sieve[i] is True]


def find_continuous_sum(target, prefix):
    answer = 0
    start, end = 0, 1
    while end < len(prefix):
        if prefix[end]-prefix[start] == target:
            answer += 1
            start += 1
        elif prefix[end]-prefix[start] > target:
            start += 1
        else:
            end += 1
    return answer


prime_prefix = find_prefix_sum(n)
result = find_continuous_sum(n, prime_prefix)
print(result)
