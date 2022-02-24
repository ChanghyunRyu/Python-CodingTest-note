n, k = map(int, input().split())
data = list(map(int, input().split()))
# 높이만큼 잘라서 얻은 양을 줄세우면 이진탐색 형태로 구현이 가능 -> Fail(시간초과)
# 자체 해결 x
# 실수: result = mid 부분을 넣어놓지 않았음.

start = 0
end = max(data)

result = 0
while start <= end:
    mid = (start+end)//2
    total = 0
    for rice in data:
        if rice > mid:
            total += rice-mid
    if total > k:
        start = mid+1
    else:
        result = mid
        end = mid-1

print(result)
