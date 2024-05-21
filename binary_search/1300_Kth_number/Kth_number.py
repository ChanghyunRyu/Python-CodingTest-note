n = int(input())
k = int(input())

start = 0
end = n*n
result = 0
while start <= end:
    mid = (start+end)//2
    count = 0
    for i in range(1, n+1):
        count += min(n, mid//i)
    if count >= k:
        result = mid
        end = mid-1
    else:
        start = mid+1
print(result)
