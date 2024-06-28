import sys


def find_greatest_common_divisor(num1, num2):
    while num1 % num2 != 0 and num2 % num1 != 0:
        if num1 > num2:
            num1 %= num2
        else:
            num2 %= num1
    return min(num1, num2)


n = int(input())
interval = []
before_tree = 0
for _ in range(n):
    tree = int(sys.stdin.readline().rstrip())
    if before_tree != 0:
        interval.append(tree-before_tree)
    before_tree = tree

divisor = find_greatest_common_divisor(interval[0], interval[1])
for i in range(2, len(interval)):
    divisor = find_greatest_common_divisor(divisor, interval[i])

answer = 0
for i in interval:
    answer += (i//divisor)-1
print(answer)
