def find_prime_number(number):
    is_prime = [True]*(2*number+1)
    is_prime[1] = False
    end = int((number+1)**0.5)
    for i in range(2, end+1):
        if is_prime[i]:
            for j in range(i+i, number+1, i):
                is_prime[j] = False
    return [i for i in range(2, number+1) if is_prime[i]]


def return_bertrand(number):
    n_2_list = find_prime_number(number*2)
    n_list = find_prime_number(number)
    return len(n_2_list)-len(n_list)


while True:
    n = int(input())
    if n == 0:
        break
    print(return_bertrand(n))
