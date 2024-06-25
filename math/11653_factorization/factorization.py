n = int(input())

if n != 1:
    for i in range(2, (n//2)+1):
        while n % i == 0:
            print(i)
            n = n//i
    if n != 1:
        print(n)
