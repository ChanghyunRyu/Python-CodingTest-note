import sys
import heapq
n = int(input())

arr = []
for _ in range(n):
    s, e = map(int, sys.stdin.readline().split())
    arr.append((s, e))
arr.sort()

room = []
heapq.heappush(room, arr[0][1])

for i in range(1, n):
    if arr[i][0] < room[0]:
        heapq.heappush(room, arr[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, arr[i][1])

print(len(room))
