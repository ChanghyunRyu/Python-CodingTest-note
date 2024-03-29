arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
t = 7


def binary_search(target, arr, start, end):
    mid = (start + end) // 2
    if start > mid:
        return None
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(target, arr, start, mid - 1)
    else:
        return binary_search(target, arr, mid+1, end)


result = binary_search(t, arr, 0, len(arr)-1)
if result is None:
    print('Can not find')
else:
    print(result)
