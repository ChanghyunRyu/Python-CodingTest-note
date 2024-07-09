m, n = map(int, input().split())


def find_prime_number(start, number):
    is_prime = [True]*(number+1)
    is_prime[1] = False
    end = int((number+1)**0.5)
    for i in range(2, end+1):
        if is_prime[i]:
            for j in range(i+i, number+1, i):
                is_prime[j] = False
    return [i for i in range(start, number+1) if is_prime[i]]


prime_numbers = find_prime_number(m, n)
for prime_number in prime_numbers:
    print(prime_number)
