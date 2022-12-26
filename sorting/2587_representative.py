import sys

num = []
for i in range(5):
    num.append(int(sys.stdin.readline()))

num.sort()
result = 0
for n in num:
    result += n
print(int(result/5))
print(num[2])
