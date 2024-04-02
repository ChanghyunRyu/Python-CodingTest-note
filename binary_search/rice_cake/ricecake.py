n, m = map(int, input().split())
ricecake = list(map(int, input().split()))
ricecake.sort()
start, end = 0, ricecake[len(ricecake)-1]

while start < end:
    mid = (start+end)//2
    sum = 0
    for r in ricecake:
        if r > mid:
            sum += r - mid
    if sum < m:
        start, end = start, mid-1
    elif sum == m:
        break
    else:
        start, end = mid+1, end

print(mid)
