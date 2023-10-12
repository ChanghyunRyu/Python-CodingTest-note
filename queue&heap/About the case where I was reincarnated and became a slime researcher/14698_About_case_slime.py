import sys
import heapq

t = int(input())
result = []
for _ in range(t):
    n = int(sys.stdin.readline())
    slime = list(map(int, sys.stdin.readline().split()))
    heapq.heapify(slime)

    elc = 1
    while len(slime) > 1:
        s1 = heapq.heappop(slime)
        s2 = heapq.heappop(slime)

        elc *= (s1*s2) % 1000000007
        heapq.heappush(slime, s1*s2)
    result.append(elc)

for r in result:
    print(r%1000000007)
