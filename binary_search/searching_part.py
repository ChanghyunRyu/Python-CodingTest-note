n = int(input())
data_1 = list(map(int, input().split()))
m = int(input())
data_2 = list(map(int, input().split()))


def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    if array[mid] == target:
        return mid
    if array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)


data_1.sort()
for data in data_2:
    if binary_search(data_1, data, 0, n-1) is not None:
        print('yes', end=' ')
    else:
        print('no', end=' ')

