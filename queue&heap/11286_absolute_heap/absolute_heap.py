import sys
import heapq

n = int(input())
q = []
for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    if num == 0:
        if q:
            print(heapq.heappop(q)[1])
        else:
            print(0)
    else:
        heapq.heappush(q, (abs(num), num))
