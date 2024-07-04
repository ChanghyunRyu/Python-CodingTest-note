n = int(input())
nums = list(map(int, input().split()))
target = int(input())

nums.sort()
answer = 0
start, end = 0, len(nums)-1
while start < end:
    if nums[start]+nums[end] > target:
        end -= 1
    elif nums[start]+nums[end] == target:
        answer += 1
        start += 1
    else:
        start += 1

print(answer)
