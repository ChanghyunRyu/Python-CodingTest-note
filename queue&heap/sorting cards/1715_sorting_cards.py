import sys
import heapq

n = int(input())
cards = []
for _ in range(n):
    cards.append(int(sys.stdin.readline()))
heapq.heapify(cards)

result = 0
while len(cards) > 1:
    c1 = heapq.heappop(cards)
    c2 = heapq.heappop(cards)
    heapq.heappush(cards, c1+c2)
    result += c1+c2

print(result)
