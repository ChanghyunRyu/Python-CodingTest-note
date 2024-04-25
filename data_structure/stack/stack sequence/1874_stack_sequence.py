import sys
n = int(input())

seq = []
for _ in range(n):
    seq.append(int(sys.stdin.readline()))
result = []

start = 0
stack = [0]
for num in seq:
    if num - start > 0:
        for i in range(start, num):
            stack.append(i+1)
            result.append('+')
    elif stack[len(stack)-1] > num:
        result = ['NO']
        break
    result.append('-')
    start = max(stack.pop(), start)

for r in result:
    print(r)
