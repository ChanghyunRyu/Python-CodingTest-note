def find_least_common_multiple(num1, num2):
    mul1, mul2 = num1, num2
    while num1 != num2:
        if num1 > num2:
            num2 += mul2
        else:
            num1 += mul1
    return num1


a, b = map(int, input().split())
print(find_least_common_multiple(a, b))
