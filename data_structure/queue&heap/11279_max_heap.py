# python sort O(n) = n*log(n)
# n = 100000(max)
# x = 0 => O(1), x != 0 => O(nlog(n))
import sys
import heapq

heap = []
n = int(input())
for _ in range(n):
    k = int(sys.stdin.readline())
    if k == 0:
        if len(heap) == 0:
            print(0)
        else:
            print((-1)*heapq.heappop(heap))
    else:
        heapq.heappush(heap, (-1)*k)
