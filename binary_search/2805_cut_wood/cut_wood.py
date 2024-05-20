n, m = map(int, input().split())
woods = list(map(int, input().split()))

start = 0
end = max(woods)

result = 0
while start <= end:
    mid = (start+end)//2
    count = 0
    for w in woods:
        if w > mid:
            count += w-mid
    if count == m:
        result = mid
        break
    elif count > m:
        result = mid
        start = mid+1
    else:
        end = mid-1
print(result)
