n = int(input())
cities = list(map(int, input().split()))
budget = int(input())

start = 1
end = max(cities)
result = 1
while start <= end:
    mid = (start+end)//2
    count = 0
    for city in cities:
        count += min(mid, city)
    if count > budget:
        end = mid-1
    else:
        result = mid
        start = mid+1
print(result)
