import sys
n, m = map(int, input().split())
nums = list(map(int, input().split()))
prefix_sum = [0]
result = 0
for num in nums:
    result += num
    prefix_sum.append(result)
q = []
for i in range(m):
    start, end = map(int, sys.stdin.readline().split())
    q.append((start, end))

for question in q:
    start, end = question[0], question[1]
    print(prefix_sum[end]-prefix_sum[start-1])
