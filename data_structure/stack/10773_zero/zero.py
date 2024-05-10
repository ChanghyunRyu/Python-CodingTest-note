import sys
from collections import deque

k = int(input())
s = deque([])
for _ in range(k):
    num = int(sys.stdin.readline().rstrip())
    if num != 0:
        s.append(num)
    else:
        s.pop()
print(sum(s))
