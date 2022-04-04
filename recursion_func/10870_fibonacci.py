n = int(input())


def fibonacci_func(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_func(n-2) + fibonacci_func(n-1)


print(fibonacci_func(n))
