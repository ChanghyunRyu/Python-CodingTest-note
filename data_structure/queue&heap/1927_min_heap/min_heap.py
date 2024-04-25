import heapq
import sys

n = int(input())
q = []
for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    if num == 0:
        if q:
            print(heapq.heappop(q))
        else:
            print(0)
    else:
        heapq.heappush(q, num)
