def find_least_common_multiple(n1, n2):
    mul1, mul2 = n1, n2
    while n1 != n2:
        if n1 > n2:
            n2 += mul2
        else:
            n1 += mul1
    return n1


def find_greatest_common_divisor(n1, n2):
    while n1 % n2 != 0 and n2 % n1 != 0:
        if n1 > n2:
            n1 %= n2
        else:
            n2 %= n1
    return min(n1, n2)


num1, deno1 = map(int, input().split())
num2, deno2 = map(int, input().split())
lcm = find_least_common_multiple(deno1, deno2)
num_sum = num1*(lcm//deno1) + num2*(lcm//deno2)
gcd = find_greatest_common_divisor(lcm, num_sum)
print('{} {}'.format(num_sum//gcd, lcm//gcd))
