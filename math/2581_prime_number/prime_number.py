m = int(input())
n = int(input())


prime_number = {}
for i in range(2, n+1):
    is_prime = True
    for p in prime_number:
        if i % p == 0:
            is_prime = False
            break
    if is_prime:
        prime_number[i] = True

sum_of_prime = 0
min_prime = -1
for i in range(m, n+1):
    if i in prime_number:
        sum_of_prime += i
        if min_prime == -1:
            min_prime = i

if sum_of_prime == 0:
    print(-1)
else:
    print(sum_of_prime)
    print(min_prime)
