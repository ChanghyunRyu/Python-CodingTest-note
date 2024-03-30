arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 7

start, end = 0, len(arr)-1
result = None
while start <= end:
    mid = (start+end)//2
    if arr[mid] == target:
        result = mid
        break
    elif arr[mid] < target:
        start, end = mid+1, end
    else:
        start, end = 0, mid-1

if result is None:
    print("None")
else:
    print(result)
