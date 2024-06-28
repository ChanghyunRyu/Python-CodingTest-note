import sys


def find_least_common_multiple(num1, num2):
    mul1, mul2 = num1, num2
    while num1 != num2:
        if num1 > num2:
            num2 += mul2
        else:
            num1 += mul1
    return num1


t = int(input())
answer = []
for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    answer.append(find_least_common_multiple(a, b))

for a in answer:
    print(a)
