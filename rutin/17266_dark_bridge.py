n = int(input())
m = int(input())
lamp = list(map(int, input().split()))


def check_height(h, l):
    last = 0
    for now in l:
        if now-h > last:
            return False
        last = now+h
    if last < n:
        return False
    else:
        return True


start = 1
end = 100000
result = end
while start <= end:
    mid = (start + end) // 2
    if check_height(mid, lamp):
        result = mid
        end = mid-1
    else:
        start = mid+1
print(result)
