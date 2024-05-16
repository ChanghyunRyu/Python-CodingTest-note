n = int(input())
arr = list(map(int, input().split()))
arr.sort()
m = int(input())
nums = list(map(int, input().split()))


def bisearch(target):
    start = 0
    end = len(arr)
    while start < end:
        mid = (start+end)//2
        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            start = mid+1
        else:
            end = mid
    return 0


for num in nums:
    print(bisearch(num))
