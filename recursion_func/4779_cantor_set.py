def cantor(num):
    if num == 0:
        print('-', end='')
    else:
        cantor(num - 1)
        for _ in range(3 ** (num - 1)):
            print(' ', end='')
        cantor(num - 1)


while True:
    try:
        n = int(input())
        cantor(n)
        print()
    except:
        break
