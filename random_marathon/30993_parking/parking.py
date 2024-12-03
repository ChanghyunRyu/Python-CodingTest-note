n, a, b, c = map(int, input().split())


def get_combination_number(N, C):
    temp = 1
    temp2 = 1
    for i in range(C):
        temp *= i+1
        temp2 *= N-i
    return temp2//temp


result = 1
result *= get_combination_number(n, a)
n -= a
result *= get_combination_number(n, b)
print(result)
