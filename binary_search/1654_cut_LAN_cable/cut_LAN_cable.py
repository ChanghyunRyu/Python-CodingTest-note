import sys

k, n = map(int, input().split())
cables = []
for _ in range(k):
    cables.append(int(sys.stdin.readline().rstrip()))

start = 1
end = max(cables)

result = 0
while start <= end:
    mid = (start+end)//2
    count = 0
    for c in cables:
        count += c//mid
    if count < n:
        end = mid-1
    else:
        result = mid
        start = mid+1
print(result)
