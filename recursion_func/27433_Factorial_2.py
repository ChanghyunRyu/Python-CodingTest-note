def fac(num):
    if num == 0 or num == 1:
        return 1
    else:
        return fac(num-1)*num


n = int(input())
print(fac(n))
