n, m = map(int, input().split())
woods = list(map(int, input().split()))

start = 0
end = max(woods)

result = 0
while start <= end:
    mid = (start+end)//2
    total = 0
    for wood in woods:
        if wood > mid:
            total += wood-mid
    if total < m:
        end = mid-1
    else:
        result = mid
        start = mid+1

print(result)
