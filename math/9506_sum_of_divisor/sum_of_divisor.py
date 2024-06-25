import sys


def check_perfect_number(n):
    divisor = []
    for i in range(1, (n//2)+1):
        if n % i == 0:
            divisor.append(i)
    if sum(divisor) == n:
        return True, divisor
    return False, []


def print_perfect_number(n, divisor):
    print(n, end=' ')
    print('=', end=' ')
    for i in range(len(divisor)):
        print(divisor[i], end= ' ')
        if i != len(divisor)-1:
            print('+', end= ' ')
    print()


while True:
    num = int(sys.stdin.readline().rstrip())
    if num == -1:
        break
    check, divisor = check_perfect_number(num)
    if check:
        print_perfect_number(num, divisor)
    else:
        print('{} is NOT perfect.'.format(num))
