import sys
import heapq

n, k = map(int, input().split())

jewel = []
for _ in range(n):
    m, v = map(int, sys.stdin.readline().split())
    jewel.append((m, v))

backpack = []
for _ in range(k):
    backpack.append(int(sys.stdin.readline()))

jewel.sort(key=lambda x: (x[0], -x[1]))
backpack.sort()

result = 0
tmp = []

for b in backpack:
    while jewel and jewel[0][0] <= b:
        heapq.heappush(tmp, -jewel[0][1])
        heapq.heappop(jewel)
    if tmp:
        result -= heapq.heappop(tmp)

print(result)
