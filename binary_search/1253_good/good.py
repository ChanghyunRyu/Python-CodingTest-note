n = int(input())
nums = list(map(int, input().split()))
nums.sort()


def bisearch(target, numbers):
    for i in range(len(numbers)):
        start = i+1
        end = len(numbers)-1
        while start <= end:
            mid = (start+end)//2
            if numbers[i]+numbers[mid] == target:
                return True
            elif numbers[i]+numbers[mid] > target:
                end = mid-1
            else:
                start = mid+1
    return False


count = 0
for j in range(n):
    if bisearch(nums[j], nums[:j]+nums[j+1:]):
        count += 1
print(count)
