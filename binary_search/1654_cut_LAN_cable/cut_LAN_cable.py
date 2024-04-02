import sys

k, n = map(int, input().split())
cable = []
for _ in range(k):
    cable.append(int(sys.stdin.readline().rstrip()))

start, end = 1, max(cable)
result = 0

while start <= end:
    mid = (start+end)//2
    total = 0
    for c in cable:
        total += c//mid
    if total < n:
        start, end = start, mid-1
    else:
        result = mid
        start, end = mid+1, end

print(result)

