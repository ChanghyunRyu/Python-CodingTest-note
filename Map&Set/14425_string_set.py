import sys

n, m = map(int, input().split())
array = []
checks = []
for i in range(n):
    array.append(sys.stdin.readline())
for j in range(m):
    checks.append(sys.stdin.readline())

num = 0
for check in checks:
    if check in array:
        num += 1
print(num)

