import sys

nums = []
results = []

n = int(input())
for i in range(n):
    nums.append(int(sys.stdin.readline()))

start = 0
stack = [0]
for num in nums:
    if stack[len(stack)-1] > num:
        results = ['NO']
        break
    if start < num:
        for i in range(start, num):
            results.append('+')
            stack.append(i + 1)
    start = max(start, stack.pop())
    results.append('-')
for r in results:
    print(r)

