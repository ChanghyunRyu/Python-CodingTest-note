n = int(input())
seq = list(map(int, input().split()))
result = [0]

for s in seq:
    if result[-1] < s:
        result.append(s)
    else:
        start, end = 0, len(result)
        while start < end:
            mid = (start + end) // 2
            if result[mid] < s:
                start = mid + 1
            else:
                end = mid
        result[end] = s
print(len(result)-1)
