n = int(input())
arr = list(map(int, input().split()))

m = int(input())
part = list(map(int, input().split()))
arr.sort()


def binary_search(target, arr, start, end):
    if end < start:
        return None
    mid = (start+end)//2
    if arr[mid] < target:
        return binary_search(target, arr, mid+1, end)
    elif arr[mid] == target:
        return mid
    else:
        return binary_search(target, arr, start, mid-1)


for p in part:
    result = binary_search(p, arr, 0, len(arr)-1)
    if result is None:
        print('no', end=' ')
    else:
        print('yes', end= ' ')

