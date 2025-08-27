from collections import deque

n = int(input())
check = list(map(int, input().split()))
qs = list(map(int, input().split()))

m = int(input())
nums = list(map(int, input().split()))
q = deque()
for i in range(n):
    if check[i] == 0:
        q.append(qs[i])

for num in nums:
    q.appendleft(num)
    print(q.pop(), end=' ')
