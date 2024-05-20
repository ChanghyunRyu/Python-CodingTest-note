import sys

n, c = map(int, input().split())
houses = []
for _ in range(n):
    houses.append(int(sys.stdin.readline().rstrip()))
houses.sort()

start = 1
end = max(houses)
result = 0
while start <= end:
    mid = (start+end)//2
    count = 1
    now = houses[0]
    for i in range(1, len(houses)):
        if houses[i]-now >= mid:
            count += 1
            now = houses[i]
    if count < c:
        end = mid-1
    else:
        result = mid
        start = mid+1
print(result)
